# solana_client.py
# Handles interaction with Solana blockchain for storing tender, bid, and award metadata

from solana.rpc.api import Client

# Connect to Solana cluster (devnet for testing)
solana_client = Client("https://api.devnet.solana.com")

# Example function to send data to Solana (to be expanded)
def store_tender_on_chain(tender_data):
    # TODO: Implement Solana transaction logic
    # This is a placeholder for sending tender metadata to Solana smart contract
    pass

# Similarly, add functions for bids and awards