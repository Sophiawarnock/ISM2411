def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

def apply_discount(price, membership):
    if membership == "gold":
        return price * 0.80
    elif membership == "silver":
        return price * 0.90
    elif membership == "bronze":
        return price * 0.95
    else:
        return price

print(f"Gold member: ${apply_discount(100, 'gold'):.2f}")
print(f"Silver member: ${apply_discount(100, 'silver'):.2f}")
print(f"Bronze member: ${apply_discount(100, 'bronze'):.2f}")
print(f"No membership: ${apply_discount(100, 'none'):.2f}")

def final_price(price, membership, tax_rate):
    discounted_price = apply_discount(price, membership)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"Gold order: ${final_price(100, 'gold', 0.07):.2f}")
print(f"Silver order: ${final_price(100, 'silver', 0.08):.2f}")
print(f"No membership: ${final_price(100, 'none', 0.07):.2f}")

orders = [
    (100, "gold", 0.07),
    (200, "silver", 0.08),
    (150, "bronze", 0.07),
    (80, "none", 0.06)
]

for price, membership, tax_rate in orders:
    total = final_price(price, membership, tax_rate)
    print(f"{membership.title()} order total: ${total:.2f}")

total = 100

def add_sale(amount):
    total = amount
    print(f"Inside function: {total}")

add_sale(50)
print(f"Outside function: {total}")

