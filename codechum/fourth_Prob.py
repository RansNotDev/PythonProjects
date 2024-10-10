def sum_non_corner_elements(matrix, rows, cols):
    total_sum = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            total_sum += matrix[i][j]
    return total_sum
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []

print("Enter elements:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
result = sum_non_corner_elements(matrix, rows, cols)
print(f"Sum = {result}")