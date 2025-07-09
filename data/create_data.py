import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "transaction_id": range(1, 50001),
    "customer_id": np.random.randint(1, 5000, 50000),
    "product_category": np.random.choice(
        ["Electronics", "Clothing", "Books", "Home"], 50000
    ),
    "amount": np.round(np.random.uniform(10, 1000, 50000), 2),
    "transaction_date": pd.date_range("2023-01-01", periods=50000, freq="10min"),
    "store_location": np.random.choice(["NYC", "LA", "Chicago", "Houston"], 50000),
}

df = pd.DataFrame(data)

df.to_csv("transactions.csv", index=False)
df.to_parquet("transactions.parquet", index=False)
print(f"Created {len(df)} transactions")
print("Files: transactions.csv, transactions.parquet")
