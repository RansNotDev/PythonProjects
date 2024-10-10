def calculate_change(total, payment):
    if payment < total:
        print("Aicham! You have to pay properly.")
    elif payment == total:
        print("I receive exact amount.")
    else:
        change = payment - total
        print(f"Your change is {change}. Here's your change:")

        bills_and_coins = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
        for value in bills_and_coins:
            count = change // value
            if count > 0:
                if value >= 20:
                    print(f"{count} {value}-peso bill")
                else:
                    print(f"{count} {value}-peso coin")
                change %= value
total = int(input("Enter total: "))
payment = int(input("Enter payment: "))
calculate_change(total, payment)