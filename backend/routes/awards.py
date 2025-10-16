from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_awards():
    # TODO: Return list of awards for tenders
    return []

@router.post("/")
def award_tender():
    # TODO: Award tender, store award on Solana
    return {"message": "Tender awarded"}