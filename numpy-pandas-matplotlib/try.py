import numpy as np
import pandas as pd

# Set a random seed so your results are reproducible every time you run it
np.random.seed(42)
num_transactions = 5000

print("--- STEP 1: GENERATING RAW DATA WITH NUMPY ---")

# 1. Generate Transaction IDs (Sequential numbers)
tx_ids = np.arange(10000, 10000 + num_transactions)

# 2. Pick Categories and Regions using Random Choice
categories_list = ["Electronics", "Clothing", "Home & Kitchen", "Beauty", "Sports"]
regions_list = ["North", "East", "South", "West"]

# Use np.random.choice to pick categories with custom probabilities (e.g., Clothing is popular)
tx_categories = np.random.choice(
    categories_list, size=num_transactions, p=[0.2, 0.3, 0.25, 0.15, 0.1]
)
tx_regions = np.random.choice(regions_list, size=num_transactions)

# 3. Generate Realistic Purchase Amounts (Exponential Distribution)
# This ensures a lot of small/medium transactions and a few massive premium orders
tx_amounts = (
    np.random.exponential(scale=80.0, size=num_transactions) + 5.0
)  # Added $5 minimum base price

# 4. Inject Realistic Imperfections (Missing Values & Outliers)
# Let's create a boolean mask to force exactly 3% of our Sales data to be missing (NaN)
missing_mask = np.random.random(size=num_transactions) < 0.03
tx_amounts[missing_mask] = np.nan

# Let's inject a few intentional massive "system error glitches" (Outliers)
outlier_indices = np.random.choice(num_transactions, size=5, replace=False)
tx_amounts[outlier_indices] = tx_amounts[outlier_indices] * 50

print(f"[OK] Successfully generated {num_transactions} raw transaction metrics.")
print(
    f"[OK] Injected {np.isnan(tx_amounts).sum()} missing values (NaN) for data cleaning practice."
)

# 5. Pack everything neatly into a raw Pandas DataFrame for the next step
df_raw = pd.DataFrame(
    {
        "Transaction_ID": tx_ids,
        "Category": tx_categories,
        "Region": tx_regions,
        "Sales_Amount": tx_amounts,
    }
)

print("\n--- Preview of the Raw NumPy Generated Data ---")
print(df_raw.head(10))
