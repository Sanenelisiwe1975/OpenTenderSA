# OpenTender SA

**A transparent, AI-powered tender platform for South Africa**

---

## Overview

OpenTender SA is a blockchain-backed platform that makes South African public procurement **transparent, accountable, and citizen-friendly**. It records tenders, bids, and awards immutably on-chain while using AI to flag suspicious activities such as repeated vendor awards, price anomalies, and linked suppliers. A publicly accessible dashboard allows citizens, journalists, and oversight bodies to monitor tenders in real-time, ensuring fairness and responsible use of public funds.

---

## Features

* **Immutable Tender Records**: All tender actions recorded on blockchain to prevent tampering.
* **AI-based Suspicious Activity Detection**: Flags unusual bidding patterns, repeated vendor wins, or price irregularities.
* **Public Dashboard**: User-friendly interface for browsing tenders, viewing flagged activities, and downloading reports.
* **Anonymous Reporting**: Secure whistleblower portal for reporting procurement irregularities.
* **Off-chain Document Storage**: Tender documents and large files stored on IPFS or Arweave, linked via on-chain hashes.

---

## Tech Stack

| Layer          | Technology                            |
| -------------- | ------------------------------------- |
| Frontend       | React, TailwindCSS                    |
| Backend        | Node.js / Python (FastAPI)            |
| Blockchain     | Solana (on-chain tender records)      |
| Database       | PostgreSQL                            |
| AI / Analytics | Python (scikit-learn, PyTorch)        |
| File Storage   | IPFS / Arweave                        |
| Hosting        | AWS Africa Cape Town / Azure SA North |

---

## Architecture

1. **Frontend** – Citizen-facing dashboard for viewing tenders, flagged activities, and submitting reports.
2. **Backend** – Handles AI analytics, off-chain storage, and communication with Solana smart contracts.
3. **On-chain** – Solana programs store tender metadata, bid hashes, and award events immutably.
4. **Off-chain** – Large tender documents stored on decentralized storage, with references on-chain.

---

## How It Works

1. A department posts a tender → details hashed and stored on-chain.
2. Vendors submit bids → bid hashes recorded on-chain.
3. AI analyzes bids and past data → flags suspicious patterns.
4. Dashboard displays tenders, flagged issues, and analytics for public review.
5. Whistleblowers submit reports securely → routed to oversight bodies.

---

## Impact

* **Transparency**: Every tender and bid is auditable and immutable.
* **Accountability**: Suspicious activities are flagged automatically.
* **Public Empowerment**: Citizens and journalists gain actionable insights.
* **Fraud Prevention**: Early detection reduces corruption risks and improves fund allocation.

---

## Installation (Hackathon Demo)

```bash
# Clone the repo
git clone https://github.com/yourusername/opentender-sa.git
cd opentender-sa

# Install dependencies
npm install

# Start frontend
npm run dev

# Backend (Python)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## Contributing

We welcome contributions! You can help with:

* Smart contract development (Solana/Rust)
* AI model improvement for flagging anomalies
* Frontend UX enhancements
* Integration with additional open data sources

---

## License

MIT License – OpenTender SA is free and open for civic-tech development.

