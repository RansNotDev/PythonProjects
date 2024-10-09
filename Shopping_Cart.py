item = input("What Item would you like to buy?: ")
price = float(input("What is the price? : "))
quantity = int(input("How many would you like? : "))
total = price * quantity
print(f"Item Name: {item}\nquantity: {quantity} \nTotal Amount to Pay: ₱{total}")