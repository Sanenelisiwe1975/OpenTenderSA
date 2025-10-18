"""
Test script for integrating the Solana smart contract with the backend.
"""

from solana_client import SolanaClient, solana_client
from solana.keypair import Keypair
from solana.rpc.commitment import Confirmed
import json
import os
from datetime import datetime
from dotenv import load_dotenv

def test_tender_flow():
    """Test the full tender flow with the Solana blockchain."""
    
    # Load environment variables
    load_dotenv()
    
    print("Starting integration test...")
    
    # Initialize the Solana client
    client = SolanaClient()
    
    try:
        # 1. Create a test tender
        tender_data = {
            "id": "TEST_TENDER_001",
            "title": "Test Road Construction Project",
            "description": "Construction of a 5km test road",
            "department": "Transport",
            "province": "Gauteng",
            "deadline": str(datetime.now()),
            "document_hash": "QmTestHash123"  # IPFS hash of tender documents
        }
        
        print("\n1. Creating tender on Solana...")
        create_result = client.create_tender(
            tender_id=tender_data["id"],
            doc_hash=tender_data["document_hash"]
        )
        
        if not create_result["success"]:
            raise Exception(f"Failed to create tender: {create_result['error']}")
        
        tender_account = create_result["tender_account"]
        print(f"Tender created successfully: {json.dumps(create_result, indent=2)}")
        
        # 2. Submit a test bid
        print("\n2. Creating test bidder keypair...")
        bidder_secret = os.getenv("TEST_BIDDER_KEY")
        test_bidder = Keypair() if not bidder_secret else Keypair.from_secret_key(bytes.fromhex(bidder_secret))
        
        print(f"Test bidder public key: {test_bidder.public_key}")
        
        # Request airdrop for test account on devnet
        if os.getenv("SOLANA_RPC_URL", "").endswith("devnet.solana.com"):
            print("\nRequesting airdrop for test bidder...")
            airdrop_result = solana_client.request_airdrop(
                test_bidder.public_key,
                2_000_000_000,  # 2 SOL
                Confirmed
            )
            print(f"Airdrop result: {json.dumps(airdrop_result, indent=2)}")
        
        bid_data = {
            "tender_id": tender_data["id"],
            "amount": 1_000_000_000,  # 1 SOL in lamports
            "document_hash": "QmBidDocHash456"  # IPFS hash of bid documents
        }
        
        print("\n3. Submitting bid...")
        bid_result = client.submit_bid(
            tender_id=bid_data["tender_id"],
            amount=bid_data["amount"],
            doc_hash=bid_data["document_hash"],
            bidder_keypair=test_bidder
        )
        
        if not bid_result["success"]:
            raise Exception(f"Failed to submit bid: {bid_result['error']}")
            
        print(f"Bid submitted successfully: {json.dumps(bid_result, indent=2)}")
        
        # 3. Award the tender
        print("\n3. Awarding tender...")
        award_result = client.award_tender(
            tender_id=tender_data["id"],
            winner=test_bidder.public_key,
            amount=bid_data["amount"]
        )
        
        if not award_result["success"]:
            raise Exception(f"Failed to award tender: {award_result['error']}")
            
        print(f"Tender awarded successfully: {json.dumps(award_result, indent=2)}")
        
        # 4. Verify final tender state
        print("\n4. Verifying tender state...")
        tender_info = client.get_tender(tender_account)
        
        if tender_info is None:
            raise Exception("Failed to fetch tender data")
            
        print(f"Final tender state: {json.dumps(tender_info, indent=2)}")
        
        # 5. Close tender (cleanup)
        print("\n5. Closing tender...")
        close_result = client.close_tender(tender_data["id"])
        
        if not close_result["success"]:
            raise Exception(f"Failed to close tender: {close_result['error']}")
            
        print(f"Tender closed successfully: {json.dumps(close_result, indent=2)}")
        
        print("\nAll integration tests completed successfully!")
        
    except Exception as e:
        print(f"\nTest failed: {str(e)}")
        raise

if __name__ == "__main__":
    test_tender_flow()