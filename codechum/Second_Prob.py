import math

def build_house(n):
    # Roof construction (3 rows)
    roof_height = 3
    roof_widths = [n + 8, n + 4, n]  # widths for each row of the roof

    # Centering the roof
    for i in range(roof_height):
        spaces = (roof_widths[0] + 4) // 2 - (roof_widths[i] // 2)  # Calculate leading spaces
        print(' ' * spaces + '*' * roof_widths[i])

    # Body construction (height of ceil(n / 2))
    house_height = math.ceil(n / 2)
    for _ in range(house_height):
        spaces = (roof_widths[0] + 4) // 2 - (n // 2)  # Center the house body
        print(' ' * spaces + '*' * n)

# Input
n = int(input("Enter house width: "))

# Build the house
build_house(n)