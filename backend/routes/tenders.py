from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_tenders():
    # TODO: Return list of tenders from DB
    return []

@router.post("/")
def create_tender():
    # TODO: Create new tender, store metadata on Solana, upload docs to IPFS
    return {"message": "Tender created"}