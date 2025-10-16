from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_bids():
    # TODO: Return list of bids for a tender
    return []

@router.post("/")
def submit_bid():
    # TODO: Submit bid, store hash on Solana
    return {"message": "Bid submitted"}