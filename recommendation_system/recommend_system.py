
import pandas as pd


products = {
    "Electronics": [
        "iPhone 15",
        "Samsung Galaxy S24",
        "MacBook Air",
        "Dell XPS Laptop"
    ],

    "Audio": [
        "Sony Headphones",
        "Boat Earbuds",
        "JBL Speaker",
        "Noise Airbuds"
    ],

    "Fashion": [
        "Nike Running Shoes",
        "Adidas Sneakers",
        "Puma Hoodie",
        "Levis Jacket"
    ],

    "Gaming": [
        "Gaming Mouse",
        "Mechanical Keyboard",
        "Gaming Chair",
        "PlayStation 5"
    ]
}


print("\n========================================")
print("     PRODUCT RECOMMENDATION SYSTEM")
print("========================================")

print("\nAvailable Categories:\n")

for category in products.keys():
    print("-", category)



user_category = input("\nEnter your favorite category: ")



print("\nRecommended Products:\n")

found = False

for category, items in products.items():

    if category.lower() == user_category.lower():

        found = True

        for product in items:
            print("•", product)


if not found:
    print("Category not found.")