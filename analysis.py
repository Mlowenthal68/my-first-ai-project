import numpy as np
import pandas as pd
import requests

# Sample sales data
data = {
    "product": ["Widget A", "Widget B", "Widget C", "Widget D", "Widget E"],
    "category": ["Electronics", "Clothing", "Electronics", "Food", "Clothing"],
    "units_sold": [152, 340, 89, 512, 278],
    "unit_price": [49.99, 19.99, 89.99, 4.99, 34.99],
    "rating": [4.2, 3.8, 4.7, 4.5, 3.9],
}

df = pd.DataFrame(data)
df["revenue"] = df["units_sold"] * df["unit_price"]

print("=== Sales Data ===")
print(df.to_string(index=False))

print("\n=== Summary Statistics ===")
print(df[["units_sold", "unit_price", "revenue", "rating"]].describe().round(2))

print("\n=== Revenue by Category ===")
category_summary = df.groupby("category").agg(
    total_revenue=("revenue", "sum"),
    avg_rating=("rating", "mean"),
    products=("product", "count"),
).round(2)
print(category_summary)

print("\n=== Top Product by Revenue ===")
top = df.loc[df["revenue"].idxmax()]
print(f"{top['product']} — ${top['revenue']:,.2f}")

print("\n=== NumPy Stats on Revenue ===")
revenues = df["revenue"].values
print(f"Mean:   ${np.mean(revenues):,.2f}")
print(f"Median: ${np.median(revenues):,.2f}")
print(f"Std:    ${np.std(revenues):,.2f}")

print("\n=== Fetching Sample External Data (requests) ===")
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    post = response.json()
    print(f"Title: {post['title']}")
    print(f"Body:  {post['body'][:80]}...")
else:
    print("Request failed.")
