import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(7)
Path("data/raw").mkdir(parents=True, exist_ok=True)

# Products
products = pd.DataFrame({
    "product_code": [f"P{str(i).zfill(4)}" for i in range(1, 51)],
    "product_name": [f"Product {i}" for i in range(1, 51)],
    "category": np.random.choice(["Electronics","Grocery","Clothing","Home","Beauty"], 50),
    "brand": np.random.choice(["Acme","Zenith","Nova","Orion","Vertex"], 50),
})
products.to_csv("data/raw/products.csv", index=False)

# Customers
customers = pd.DataFrame({
    "customer_code": [f"C{str(i).zfill(5)}" for i in range(1, 301)],
    "gender": np.random.choice(["M","F","Other"], 300, p=[0.48,0.48,0.04]),
    "age_group": np.random.choice(["18-25","26-35","36-45","46-60","60+"], 300),
    "city": np.random.choice(["New York","Chicago","Dallas","Seattle","Miami","Boston"], 300),
})
customers.to_csv("data/raw/customers.csv", index=False)

# Stores
stores = pd.DataFrame({
    "store_code": [f"S{str(i).zfill(3)}" for i in range(1, 21)],
    "store_name": [f"Store {i}" for i in range(1, 21)],
    "region": np.random.choice(["North","South","East","West"], 20),
    "state": np.random.choice(["NY","IL","TX","WA","FL","MA","CA","GA"], 20),
})
stores.to_csv("data/raw/stores.csv", index=False)

# Sales
dates = pd.date_range("2024-01-01", "2026-12-31", freq="D")
n = 8000

sales = pd.DataFrame({
    "sales_id": [f"T{str(i).zfill(7)}" for i in range(1, n+1)],
    "order_id": [f"O{str(i//2+1).zfill(6)}" for i in range(n)],
    "sale_date": np.random.choice(dates, n),
    "product_code": np.random.choice(products["product_code"], n),
    "customer_code": np.random.choice(customers["customer_code"], n),
    "store_code": np.random.choice(stores["store_code"], n),
    "quantity": np.random.randint(1, 6, n),
})

price = np.random.uniform(5, 250, n).round(2)
sales["revenue"] = (sales["quantity"] * price).round(2)
sales["discount"] = (sales["revenue"] * np.random.choice([0,0.05,0.10,0.15], n, p=[0.55,0.2,0.2,0.05])).round(2)
sales["profit"] = (sales["revenue"] - sales["discount"] - (sales["revenue"] * np.random.uniform(0.4, 0.75, n))).round(2)

sales.to_csv("data/raw/sales.csv", index=False)

print("✅ Demo CSV files generated successfully in data/raw/")
