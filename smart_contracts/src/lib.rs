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
    system_instruction,
    program::invoke,
    sysvar::{rent::Rent, Sysvar},
    clock::Clock,
};

#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct Tender {
    pub id: String,
    pub authority: Pubkey,
    pub doc_hash: String,
    pub status: TenderStatus,
    pub created_at: i64,
    pub updated_at: i64,
}

#[derive(BorshSerialize, BorshDeserialize, Debug, PartialEq)]
pub enum TenderStatus {
    Open,
    Closed,
    Awarded,
}

#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct Bid {
    pub tender_id: String,
    pub bidder: Pubkey,
    pub amount: u64,
    pub doc_hash: String,
    pub submitted_at: i64,
}

#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct Award {
    pub tender_id: String,
    pub winner: Pubkey,
    pub amount: u64,
    pub awarded_at: i64,
}

impl Tender {
    pub fn try_to_vec(&self) -> Result<Vec<u8>, std::io::Error> {
        let mut vec = Vec::new();
        self.serialize(&mut vec)?;
        Ok(vec)
    }
}

impl Bid {
    pub fn try_to_vec(&self) -> Result<Vec<u8>, std::io::Error> {
        let mut vec = Vec::new();
        self.serialize(&mut vec)?;
        Ok(vec)
    }
}

impl Award {
    pub fn try_to_vec(&self) -> Result<Vec<u8>, std::io::Error> {
        let mut vec = Vec::new();
        self.serialize(&mut vec)?;
        Ok(vec)
    }
}

pub enum Instruction {
    CreateTender {
        id: String,
        doc_hash: String,
    },
    SubmitBid {
        tender_id: String,
        amount: u64,
        doc_hash: String,
    },
    AwardTender {
        tender_id: String,
        winner: Pubkey,
        amount: u64,
    },
    CloseTender {
        tender_id: String,
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
            1 => {
                let (tender_id_bytes, rest) = rest.split_at(32);
                let tender_id = String::from_utf8(tender_id_bytes.to_vec()).unwrap().trim_end_matches(char::from(0)).to_string();
                let (amount_bytes, rest) = rest.split_at(8);
                let amount = u64::from_le_bytes(amount_bytes.try_into().unwrap());
                let doc_hash = String::from_utf8(rest.to_vec()).unwrap().trim_end_matches(char::from(0)).to_string();
                Self::SubmitBid { tender_id, amount, doc_hash }
            }
            2 => {
                let (tender_id_bytes, rest) = rest.split_at(32);
                let tender_id = String::from_utf8(tender_id_bytes.to_vec()).unwrap().trim_end_matches(char::from(0)).to_string();
                let (winner_bytes, rest) = rest.split_at(32);
                let winner = Pubkey::try_from(winner_bytes).map_err(|_| ProgramError::InvalidInstructionData)?;
                let amount_bytes = rest.try_into().unwrap();
                let amount = u64::from_le_bytes(amount_bytes);
                Self::AwardTender { tender_id, winner, amount }
            }
            3 => {
                let tender_id = String::from_utf8(rest.to_vec()).unwrap().trim_end_matches(char::from(0)).to_string();
                Self::CloseTender { tender_id }
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
            let tender_account = next_account_info(accounts_iter)?;
            let system_program = next_account_info(accounts_iter)?;

            if !authority.is_signer {
                return Err(ProgramError::MissingRequiredSignature);
            }

            let clock = Clock::get()?;
            let tender = Tender {
                id,
                authority: *authority.key,
                doc_hash,
                status: TenderStatus::Open,
                created_at: clock.unix_timestamp,
                updated_at: clock.unix_timestamp,
            };

            let space = tender.try_to_vec()?.len();
            let rent = Rent::get()?;
            let lamports = rent.minimum_balance(space);

            invoke(
                &system_instruction::create_account(
                    authority.key,
                    tender_account.key,
                    lamports,
                    space as u64,
                    program_id,
                ),
                &[authority.clone(), tender_account.clone(), system_program.clone()],
            )?;

            tender.serialize(&mut *tender_account.try_borrow_mut_data()?)?;
        }

        Instruction::SubmitBid { tender_id, amount, doc_hash } => {
            msg!("Instruction: SubmitBid");
            let bidder = next_account_info(accounts_iter)?;
            let tender_account = next_account_info(accounts_iter)?;
            let bid_account = next_account_info(accounts_iter)?;
            let system_program = next_account_info(accounts_iter)?;

            if !bidder.is_signer {
                return Err(ProgramError::MissingRequiredSignature);
            }

            let tender = Tender::try_from_slice(&tender_account.try_borrow_data()?)?;
            if tender.status != TenderStatus::Open {
                return Err(ProgramError::InvalidAccountData);
            }

            let clock = Clock::get()?;
            let bid = Bid {
                tender_id,
                bidder: *bidder.key,
                amount,
                doc_hash,
                submitted_at: clock.unix_timestamp,
            };

            let space = bid.try_to_vec()?.len();
            let rent = Rent::get()?;
            let lamports = rent.minimum_balance(space);

            invoke(
                &system_instruction::create_account(
                    bidder.key,
                    bid_account.key,
                    lamports,
                    space as u64,
                    program_id,
                ),
                &[bidder.clone(), bid_account.clone(), system_program.clone()],
            )?;

            bid.serialize(&mut *bid_account.try_borrow_mut_data()?)?;
        }

        Instruction::AwardTender { tender_id, winner, amount } => {
            msg!("Instruction: AwardTender");
            let authority = next_account_info(accounts_iter)?;
            let tender_account = next_account_info(accounts_iter)?;
            let award_account = next_account_info(accounts_iter)?;
            let system_program = next_account_info(accounts_iter)?;

            if !authority.is_signer {
                return Err(ProgramError::MissingRequiredSignature);
            }

            let mut tender = Tender::try_from_slice(&tender_account.try_borrow_data()?)?;
            if tender.authority != *authority.key || tender.status != TenderStatus::Open {
                return Err(ProgramError::InvalidAccountData);
            }

            let clock = Clock::get()?;
            let award = Award {
                tender_id,
                winner,
                amount,
                awarded_at: clock.unix_timestamp,
            };

            tender.status = TenderStatus::Awarded;
            tender.updated_at = clock.unix_timestamp;

            let space = award.try_to_vec()?.len();
            let rent = Rent::get()?;
            let lamports = rent.minimum_balance(space);

            invoke(
                &system_instruction::create_account(
                    authority.key,
                    award_account.key,
                    lamports,
                    space as u64,
                    program_id,
                ),
                &[authority.clone(), award_account.clone(), system_program.clone()],
            )?;

            award.serialize(&mut *award_account.try_borrow_mut_data()?)?;
            tender.serialize(&mut *tender_account.try_borrow_mut_data()?)?;
        }

        Instruction::CloseTender { tender_id } => {
            msg!("Instruction: CloseTender");
            let authority = next_account_info(accounts_iter)?;
            let tender_account = next_account_info(accounts_iter)?;

            if !authority.is_signer {
                return Err(ProgramError::MissingRequiredSignature);
            }

            let mut tender = Tender::try_from_slice(&tender_account.try_borrow_data()?)?;
            if tender.authority != *authority.key || tender.status != TenderStatus::Open {
                return Err(ProgramError::InvalidAccountData);
            }

            let clock = Clock::get()?;
            tender.status = TenderStatus::Closed;
            tender.updated_at = clock.unix_timestamp;

            tender.serialize(&mut *tender_account.try_borrow_mut_data()?)?;
        }
    }

    Ok(())
}