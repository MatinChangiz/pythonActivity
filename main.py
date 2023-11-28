goods = {"phone": 400, "computer" : 1000, "car":8000, "building": 200000}

varBalance = 80000
varPurchased = []
vartotal = 0;
print("Available items in 马丁 shopping system:")
for key, item in goods.items():
    print(f"Items: {key}  ------->  Price:  ${item}")

while True:
    print(f"\nYour balance: ${varBalance}")
    varInput = input("Enter the item name to buy or (done) to stop shopping: ")

    if varInput == 'done':
        break

    if varInput in goods:
        item = goods[varInput]
        if varBalance >= item:
            varBalance -= item
            vartotal +=item
            varPurchased.append(varInput)
            print("The purchase is successful, and the corresponding fees are deducted!")
        else:
            print("The balance is insufficient.")

print("Purchased Goods:")
print(varPurchased)
print("Total purchased amount:  ")
print(vartotal)

# All assignment have been submitted to teacher
# Some more comment