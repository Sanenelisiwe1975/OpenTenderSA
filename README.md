# OpenTender SA

A transparent, AI-powered tender platform for South Africa that leverages blockchain technology for accountability in public procurement.

## Overview

OpenTender SA is a blockchain-backed platform that makes South African public procurement transparent, accountable, and citizen-friendly. It records tenders, bids, and awards immutably on Solana while using AI to flag suspicious activities.

### Key Features

- **Immutable Tender Records**: All tender actions recorded on Solana blockchain
- **AI-based Suspicious Activity Detection**: Automated flagging of unusual patterns
- **Public Dashboard**: User-friendly interface for monitoring tenders
- **Anonymous Reporting**: Secure whistleblower portal
- **Off-chain Storage**: IPFS/Arweave integration for documents

## Architecture

### Tech Stack

- **Frontend**: React + TailwindCSS
- **Backend**: Python (FastAPI)
- **Blockchain**: Solana
- **Database**: PostgreSQL
- **AI/ML**: Python (scikit-learn)
- **Storage**: IPFS/Arweave

### Components

1. **Solana Smart Contract** (`/smart_contracts`)
   - Handles tender metadata storage
   - Records bid submissions
   - Manages tender awards

2. **Backend API** (`/backend`)
   - FastAPI server for API endpoints
   - Solana program interaction
   - AI analysis integration
   - IPFS/Arweave storage management

3. **Frontend Dashboard** (`/frontend`)
   - React-based UI
   - Real-time tender monitoring
   - Interactive data visualization
   - Secure reporting interface

4. **AI Analysis** (`/ai_storage`)
   - Anomaly detection
   - Pattern recognition
   - Risk scoring

## Local Development Setup

### Prerequisites

- Node.js (v16+)
- Python (3.9+)
- Solana CLI tools
- PostgreSQL
- IPFS or Arweave node

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/OpenTenderSA.git
   cd OpenTenderSA
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   ```

4. **Smart Contract Setup**
   ```bash
   cd smart_contracts
   # Follow Solana program deployment instructions
   ```

### Running the Application

1. **Start the Backend**
   ```bash
   cd backend
   uvicorn app:app --reload
   ```

2. **Start the Frontend**
   ```bash
   cd frontend
   npm run dev
   ```

3. **Access the Application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.