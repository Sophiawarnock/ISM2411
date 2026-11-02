# ISM 2411 - Module 8
# Inventory Assignment

# Exercise 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])

# Exercise 3
print(inventory[0:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4
inventory.append("envelope")
inventory.remove("tape")
inventory.sort()
print(inventory)

# Exercise 5
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Cannot change a tuple!")

print(coords)

# Exercise 6
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
best = max(sales)
worst = min(sales)

print("Total:", total)
print("Average:", average)
print("Best:", best)
print("Worst:", worst)

# Exercise 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = price * 0.90
    discounted.append(new_price)

print(prices)
print(discounted)

# Exercise 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

count = len(high_sales)
average = sum(high_sales) / count

print(high_sales)
print("Count:", count)
print("Avg:", round(average, 2))

# Reflection:
# 1. I learned that lists can store multiple items and can be changed.
# 2. A business could use lists to track inventory and calculate sales.

