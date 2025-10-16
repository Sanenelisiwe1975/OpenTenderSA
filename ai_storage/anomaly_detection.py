# anomaly_detection.py
# Sample AI code to flag suspicious bids

import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(bids):
    # bids: list of dicts with 'vendor', 'amount', 'submitted_at'
    df = pd.DataFrame(bids)
    model = IsolationForest(contamination=0.1)
    df['amount_scaled'] = (df['amount'] - df['amount'].mean()) / df['amount'].std()
    preds = model.fit_predict(df[['amount_scaled']])
    df['flagged'] = preds == -1
    return df[df['flagged']].to_dict(orient='records')

# Example usage
if __name__ == "__main__":
    sample_bids = [
        {'vendor': 'A', 'amount': 1000, 'submitted_at': '2024-06-01'},
        {'vendor': 'B', 'amount': 5000, 'submitted_at': '2024-06-02'},
        {'vendor': 'A', 'amount': 12000, 'submitted_at': '2024-06-03'},
    ]
    flagged = detect_anomalies(sample_bids)
    print("Flagged bids:", flagged)