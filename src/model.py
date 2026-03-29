import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pickle

# Load cleaned dataset
df = pd.read_csv("../data/cleaned_data.csv")

# Convert to datetime
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# Reference date
reference_date = df['order_purchase_timestamp'].max()

# Create RFM table
rfm = df.groupby('customer_unique_id').agg({
    'order_purchase_timestamp': lambda x: (reference_date - x.max()).days,
    'order_id': 'count',
    'total_price': 'sum'
}).reset_index()

# Rename columns
rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']

print("RFM Data:")
print(rfm.head())

# Scale data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[['recency', 'frequency', 'monetary']])

# Apply KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['cluster'] = kmeans.fit_predict(rfm_scaled)

print("\nCluster Summary:")
print(rfm.groupby('cluster')[['recency', 'frequency', 'monetary']].mean())
# Save model
with open("../models/kmeans_model.pkl", "wb") as f:
    pickle.dump(kmeans, f)

# Save RFM data
rfm.to_csv("../data/rfm_data.csv", index=False)

print("\n✅ Model training complete & saved!")