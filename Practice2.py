
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
range_limit = int(input("Enter the range limit: "))

print(first_number, second_number, end=" ")

for _ in range(range_limit - 2):
    next_number = first_number + second_number
    print(next_number, end=" ")
    first_number = second_number
    second_number = next_number