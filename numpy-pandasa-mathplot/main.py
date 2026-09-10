import numpy as np
import pandas as pd

# the starting value of the random number generator is the seed 50
# this will ensure that the random numbers are generated in the same order every time starting from 50
np.random.seed(50)
num_transactions = 5000

# transactions id
txn_ids = np.arange(10000, 10000 + num_transactions)

print(f"Generated {len(txn_ids)} transaction IDs starting from 10000.")
print("Sample IDs:", txn_ids[:5], "...", txn_ids[-5:])

# categories and regions
categories = ["Electronics", "Clothing", "Home & Kitchen", "Beauty", "Sports"]
region = ["East", "West", "North", "South"]

# here we assign probabilities to the categories
# clothing is the most popular category with probability 0.3

txn_cate = np.random.choice(
    categories, size=num_transactions, p=[0.2, 0.3, 0.25, 0.15, 0.1]
)

# same for the region also
txn_region = np.random.choice(region, size=num_transactions)

# transaction amounts
# we use exponential distribution to generate realistic transaction amounts
# this ensures that there are a lot of small/medium transactions and a few massive premium orders
#  in the below code we use scale 80 it mean the average transaction amount is 80  and added the base or minimum  price 10
txn_amount = np.random.exponential(scale=80.0, size=num_transactions) + 10.0

# inject some missing values in the transaction amounts
