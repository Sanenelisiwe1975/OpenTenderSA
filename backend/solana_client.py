# solana_client.py
# Handles interaction with Solana blockchain for storing tender, bid, and award metadata

from solana.rpc.api import Client
from solana.rpc.commitment import Confirmed
from solana.keypair import Keypair
from solana.system_program import SYS_PROGRAM_ID
from solana.transaction import Transaction
from solana.publickey import PublicKey
import base58
import os
from dotenv import load_dotenv
import borsh

# Load environment variables
load_dotenv()

# Connect to Solana cluster (devnet for testing)
SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://api.devnet.solana.com")
solana_client = Client(SOLANA_RPC_URL)

# Load program ID from environment
PROGRAM_ID = PublicKey(os.getenv("PROGRAM_ID"))

class SolanaClient:
    def __init__(self):
        # Initialize with authority keypair
        self.authority = Keypair.from_secret_key(
            base58.b58decode(os.getenv("AUTHORITY_SECRET_KEY"))
        )

    def create_tender(self, tender_id: str, doc_hash: str):
        """Create a new tender on Solana blockchain"""
        try:
            # Create account for tender data
            tender_account = Keypair()
            
            # Create instruction data
            instruction_data = borsh.serialize({
                "variant": "CreateTender",
                "id": tender_id,
                "doc_hash": doc_hash,
            })

            # Build transaction
            transaction = Transaction()
            transaction.add(
                self.program.create_tender(
                    tender_id=tender_id,
                    doc_hash=doc_hash,
                    authority=self.authority.public_key,
                    tender_account=tender_account.public_key,
                    system_program=SYS_PROGRAM_ID,
                )
            )

            # Send transaction
            result = solana_client.send_transaction(
                transaction,
                self.authority,
                tender_account,
                opts={"preflight_commitment": "confirmed"},
            )

            return {
                "success": True,
                "signature": result["result"],
                "tender_account": str(tender_account.public_key)
            }

        except Exception as e:
            return {"success": False, "error": str(e)}

    def submit_bid(self, tender_id: str, amount: int, doc_hash: str, bidder_keypair: Keypair):
        """Submit a bid for a tender"""
        try:
            # Create account for bid data
            bid_account = Keypair()
            
            # Build transaction
            transaction = Transaction()
            transaction.add(
                self.program.submit_bid(
                    tender_id=tender_id,
                    amount=amount,
                    doc_hash=doc_hash,
                    bidder=bidder_keypair.public_key,
                    bid_account=bid_account.public_key,
                    system_program=SYS_PROGRAM_ID,
                )
            )

            # Send transaction
            result = solana_client.send_transaction(
                transaction,
                bidder_keypair,
                bid_account,
                opts={"preflight_commitment": "confirmed"},
            )

            return {
                "success": True,
                "signature": result["result"],
                "bid_account": str(bid_account.public_key)
            }

        except Exception as e:
            return {"success": False, "error": str(e)}

    def award_tender(self, tender_id: str, winner: PublicKey, amount: int):
        """Award a tender to a winning bid"""
        try:
            # Create account for award data
            award_account = Keypair()
            
            # Build transaction
            transaction = Transaction()
            transaction.add(
                self.program.award_tender(
                    tender_id=tender_id,
                    winner=winner,
                    amount=amount,
                    authority=self.authority.public_key,
                    award_account=award_account.public_key,
                    system_program=SYS_PROGRAM_ID,
                )
            )

            # Send transaction
            result = solana_client.send_transaction(
                transaction,
                self.authority,
                award_account,
                opts={"preflight_commitment": "confirmed"},
            )

            return {
                "success": True,
                "signature": result["result"],
                "award_account": str(award_account.public_key)
            }

        except Exception as e:
            return {"success": False, "error": str(e)}

    def close_tender(self, tender_id: str):
        """Close a tender"""
        try:
            # Build transaction
            transaction = Transaction()
            transaction.add(
                self.program.close_tender(
                    tender_id=tender_id,
                    authority=self.authority.public_key,
                )
            )

            # Send transaction
            result = solana_client.send_transaction(
                transaction,
                self.authority,
                opts={"preflight_commitment": "confirmed"},
            )

            return {
                "success": True,
                "signature": result["result"]
            }

        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_tender(self, tender_account: PublicKey):
        """Fetch tender data from Solana"""
        try:
            account_info = solana_client.get_account_info(
                tender_account,
                commitment=Confirmed,
            )
            
            if account_info["result"]["value"] is None:
                return None

            # Deserialize account data
            data = base58.b58decode(account_info["result"]["value"]["data"][0])
            tender = borsh.deserialize(data)
            
            return tender

        except Exception as e:
            return None

    def get_bid(self, bid_account: PublicKey):
        """Fetch bid data from Solana"""
        try:
            account_info = solana_client.get_account_info(
                bid_account,
                commitment=Confirmed,
            )
            
            if account_info["result"]["value"] is None:
                return None

            # Deserialize account data
            data = base58.b58decode(account_info["result"]["value"]["data"][0])
            bid = borsh.deserialize(data)
            
            return bid

        except Exception as e:
            return None