goods = {
    "1": {"name": "iPhon 20 pro max", "price": 10},
    "2": {"name": "Mac Book Pro2025", "price": 20},
    "3": {"name": "S30 Ultra", "price": 15},
    "4": {"name": "", "price": 30},
    "5": {"name": "Item 5", "price": 25}
}

# goods1 = {"phone": "400", "computer" : "1000", "car":"8000", "building": "200000"}

balance = 100
purchased_goods = []

print("List of available goods in Matin shoping system:")
for key, item in goods.items():
    print(f"{key}. {item['name']} - ${item['price']}")

while True:
    print(f"\nYour balance: ${balance}")
    choice = input("Enter the number of the item you want to purchase (or 'q' to quit): ")

    if choice == 'q':
        break

    if choice in goods:
        item = goods[choice]
        if balance >= item['price']:
            balance -= item['price']
            purchased_goods.append(item['name'])
            print(f"Purchase successful! {item['name']} added to your cart.")
        else:
            print("Insufficient balance. Please add funds.")
    else:
        print("Invalid choice. Please try again.")

print("\nThank you for shopping with us!")
print("Your Purchased Goods:")
for item in purchased_goods:
    print(item)