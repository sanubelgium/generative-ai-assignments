
# Task 1 : Product Collection
products = ["Laptop", "Smartphone", "Headphones", "Keyboard", "Mouse", "Monitor"]
print("Initial products:", products)

# tuple of one product, price is assumed in EURO
sample_product = ("Laptop", 1200.0, "Electronics")
print("Sample product tuple:", sample_product)

print("2nd product:", products[1])
print("Last product:", products[-1])

# Append new products
products.append("Joystick")
products.append("External Hard Disk")
print("Updated products:", products)

# Convert tuple to list, update price, convert back
sample_product_list = list(sample_product)
sample_product_list[1] = 1100.0
sample_product = tuple(sample_product_list)
print("Updated sample product tuple:", sample_product)


# Task 2 : Categories (Sets)
categories = [
    "Electronics", "Electronics", "Accessories",
    "Accessories", "Accessories", "Electronics",
    "Accessories", "Accessories"
]
categories_set = set(categories)
print("Initial categories set:", categories_set)

categories_set.add("Gaming")
categories_set.add("Accessories")
print("After adding categories:", categories_set)

print("Is 'Gaming' in set?", "Gaming" in categories_set)
print("Total unique categories:", len(categories_set))


# Task 3 : Product Pricing (Dictionaries)
price_dict = {
    "Laptop": 1200,
    "Smartphone": 800,
    "Headphones": 150,
    "Keyboard": 100,
    "Mouse": 50,
    "Monitor": 300
}
print("Initial prices:", price_dict)

price_dict["Joystick"] = 35
print("Added Joystick:", price_dict)

price_dict["Mouse"] = 55
print("Updated Mouse price:", price_dict)

remove_product = "External Hard Disk"
removed_price = price_dict.pop(remove_product, None)
if removed_price is None:
    print(f"{remove_product} not found, nothing removed.")
else:
    print(f"Removed {remove_product}.")

average_price = sum(price_dict.values()) / len(price_dict)
print("Average price:", average_price)

max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)
print("Maximum Price:", max_product, price_dict[max_product])
print("Minimum Price:", min_product, price_dict[min_product])


# Task 4 : Combined Operations

catalog = []
for product, category in zip(products, categories):
    if product in price_dict:
        catalog.append((product, price_dict[product], category))

print("Catalog:")
for item in catalog:
    print(item)

category_to_products = {}
for product, _, category in catalog:
    category_to_products.setdefault(category, []).append(product)

print("Category to products:", category_to_products)

max_category = max(category_to_products, key=lambda c: len(category_to_products[c]))
print("Category with most products:", max_category)
print("Products in that category:", category_to_products[max_category])
