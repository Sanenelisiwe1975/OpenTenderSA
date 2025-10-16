# ai_analysis.py
# Handles AI-based suspicious activity detection

import pandas as pd
from sklearn.ensemble import IsolationForest

# Example function to flag suspicious bids

def flag_suspicious_bids(bid_data):
    # bid_data: pandas DataFrame with columns ['vendor', 'amount', 'submitted_at']
    model = IsolationForest(contamination=0.1)
    bid_data['amount_scaled'] = (bid_data['amount'] - bid_data['amount'].mean()) / bid_data['amount'].std()
    preds = model.fit_predict(bid_data[['amount_scaled']])
    bid_data['flagged'] = preds == -1
    return bid_data[bid_data['flagged']]

# TODO: Expand with more features (vendor dominance, deadline manipulation, etc.)