number = int(input("Enter the number for the multiplication table: "))
range_limit = int(input("Enter the range limit: "))

for i in range(1, range_limit + 1):
    print(f"{number} x {i} = {number * i}")