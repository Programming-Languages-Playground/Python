orders = ["Hitest", "Aman", "Divyanshu"]

for name in orders:
    print(f"Order ready for {name}");

# ---------- Enumerate

menu = ["Green", "Lemon", "spiced", "Mint"]

for idx, menu in enumerate(menu, start = 1):
    print(f"Menu item is {idx}: {menu}")

# ---------- Zip

names = ["Hitest", "Aman", "Divyanshu"]
amount = [10, 20, 20]

for name, amount in zip(names, amount):
    print(f"{name}, your total is: {amount}")

# ---------- While loop

temperature = 40

while(temperature < 100):
    print(f"Tea temp: {temperature}")
    temperature += 15

print("Tea is ready to boil!")
