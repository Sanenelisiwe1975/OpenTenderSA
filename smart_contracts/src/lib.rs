// Tender.sol (Rust-based Solana program template)
// Stores tender metadata and bid hashes on-chain

use borsh::{BorshDeserialize, BorshSerialize};
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
};

#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct Tender {
    pub id: String,
    pub authority: Pubkey,
    pub doc_hash: String, // Off-chain storage hash
}

pub enum Instruction {
    CreateTender {
        id: String,
        doc_hash: String,
    },
}

impl Instruction {
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let (tag, rest) = input.split_first().ok_or(ProgramError::InvalidInstructionData)?;
        Ok(match tag {
            0 => {
                let (id_bytes, rest) = rest.split_at(32);
                let id = String::from_utf8(id_bytes.to_vec()).unwrap().trim_end_matches(char::from(0)).to_string();
                let doc_hash = String::from_utf8(rest.to_vec()).unwrap().trim_end_matches(char::from(0)).to_string();
                Self::CreateTender { id, doc_hash }
            }
            _ => return Err(ProgramError::InvalidInstructionData),
        })
    }
}

entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = Instruction::unpack(instruction_data)?;
    let accounts_iter = &mut accounts.iter();

    match instruction {
        Instruction::CreateTender { id, doc_hash } => {
            msg!("Instruction: CreateTender");
            let authority = next_account_info(accounts_iter)?;
            if !authority.is_signer {
                return Err(ProgramError::MissingRequiredSignature);
            }

            let tender_account = next_account_info(accounts_iter)?;
            let mut tender_data = tender_account.try_borrow_mut_data()?;
            let tender = Tender {
                id,
                authority: *authority.key,
                doc_hash,
            };
            tender.serialize(&mut *tender_data)?;
        }
    }

    Ok(())
}