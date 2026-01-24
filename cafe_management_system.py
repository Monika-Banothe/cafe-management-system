# %%

menu = {
    'Pizza': 240,
    'Pasta': 140,
    'Burger': 80,
    'Salad': 120,
    'Tea': 40,
    'Coffee': 60
}

print("Welcome to the Unique Cafe")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

while True:
    item = input("\nEnter the item you want to order: ").title()

    if item in menu:
        order_total += menu[item]
        print(f"{item} added to your order.")
    else:
        print(f"{item} is not available.")

    another_order = input("Do you want to order another item? (Yes/No): ")

    if another_order.lower() == "no":
        break

print(f"\nTotal amount to pay: Rs{order_total}")



