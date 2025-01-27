import csv
import timeit
from BTrees.OOBTree import OOBTree

# Step 1: Load the data from the provided CSV file
file_path = "./generated_items_data.csv"

data = []
with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(
            {
                "ID": int(row["ID"]),
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"]),
            }
        )


# Step 2: Define structures to store the data
class OOBTreeWrapper:
    def __init__(self):
        self.tree = OOBTree()

    def add(self, key, value):
        self.tree[key] = value

    def range_query(self, min_price, max_price):
        return [
            value
            for key, value in self.tree.items()
            if min_price <= value["Price"] <= max_price
        ]

    def range_query_with_items(self, min_price, max_price):
        return [
            value
            for key, value in self.tree.items(min=min_price, max=max_price)
            if min_price <= value["Price"] <= max_price
        ]


# Step 3: Define functions to add items
def add_item_to_tree(tree, item_id, item_data):
    tree.add(item_id, item_data)


def add_item_to_dict(storage, item_id, item_data):
    storage[item_id] = item_data


# Initialize structures
oob_tree = OOBTreeWrapper()
dict_storage = {}

# Step 4: Populate the structures with data from the CSV
for row in data:
    item_id = row["ID"]
    item_data = {
        "Name": row["Name"],
        "Category": row["Category"],
        "Price": row["Price"],
    }
    add_item_to_tree(oob_tree, item_id, item_data)
    add_item_to_dict(dict_storage, item_id, item_data)


# Step 5: Define range query functions
def range_query_dict(storage, min_price, max_price):
    return [
        value for value in storage.values() if min_price <= value["Price"] <= max_price
    ]


# Step 6: Measure performance of range queries
def measure_performance(func, *args, repeats=100):
    total_time = timeit.timeit(lambda: func(*args), number=repeats)
    return total_time


# Determine price range dynamically
min_price = min(item["Price"] for item in data)
max_price = max(item["Price"] for item in data)

# Measure performance for OOBTree and dict
tree_time = measure_performance(oob_tree.range_query_with_items, min_price, max_price)
dict_time = measure_performance(range_query_dict, dict_storage, min_price, max_price)

# Step 7: Output results
print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
print(f"Total range_query time for Dict: {dict_time:.6f} seconds")
