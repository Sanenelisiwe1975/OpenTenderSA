from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import tenders, bids, awards, reports

app = FastAPI(title="OpenTender SA API")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers for modular API endpoints
app.include_router(tenders.router, prefix="/tenders", tags=["Tenders"])
app.include_router(bids.router, prefix="/bids", tags=["Bids"])
app.include_router(awards.router, prefix="/awards", tags=["Awards"])
app.include_router(reports.router, prefix="/reports", tags=["Reports"])

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to OpenTender SA API"}