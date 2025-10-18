import os
from solana_client import SolanaClient
from solana.keypair import Keypair
import json

def test_tender_flow():
    # Initialize Solana client
    client = SolanaClient()
    
    # Test data
    tender_id = "TEST001"
    doc_hash = "QmTest123"
    amount = 1000000  # 1 SOL in lamports
    
    # Create a test bidder keypair
    bidder = Keypair()
    
    print("Testing Solana integration...")
    
    try:
        # 1. Create tender
        print("\n1. Creating tender...")
        create_result = client.create_tender(tender_id, doc_hash)
        if not create_result["success"]:
            raise Exception(f"Failed to create tender: {create_result['error']}")
        print(f"Tender created successfully: {json.dumps(create_result, indent=2)}")
        
        tender_account = create_result["tender_account"]
        
        # 2. Submit bid
        print("\n2. Submitting bid...")
        bid_result = client.submit_bid(tender_id, amount, "QmBidDoc123", bidder)
        if not bid_result["success"]:
            raise Exception(f"Failed to submit bid: {bid_result['error']}")
        print(f"Bid submitted successfully: {json.dumps(bid_result, indent=2)}")
        
        # 3. Award tender
        print("\n3. Awarding tender...")
        award_result = client.award_tender(tender_id, bidder.public_key, amount)
        if not award_result["success"]:
            raise Exception(f"Failed to award tender: {award_result['error']}")
        print(f"Tender awarded successfully: {json.dumps(award_result, indent=2)}")
        
        # 4. Verify tender status
        print("\n4. Verifying tender status...")
        tender_data = client.get_tender(tender_account)
        if tender_data is None:
            raise Exception("Failed to fetch tender data")
        print(f"Tender status: {json.dumps(tender_data, indent=2)}")
        
        print("\nAll tests completed successfully!")
        
    except Exception as e:
        print(f"\nTest failed: {str(e)}")

if __name__ == "__main__":
    test_tender_flow()