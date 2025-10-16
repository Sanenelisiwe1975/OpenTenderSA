# storage.py
# Handles off-chain storage of documents using IPFS or Arweave

import ipfshttpclient

# Connect to local IPFS node
ipfs_client = ipfshttpclient.connect()

def upload_document_to_ipfs(file_path):
    # Uploads a file to IPFS and returns the hash
    res = ipfs_client.add(file_path)
    return res['Hash']

# TODO: Add Arweave integration as needed