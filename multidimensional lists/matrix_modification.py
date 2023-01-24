size = int(input())
matrix = [[int(n) for n in input().split()] for _ in range(size)]

command = input().split()

while command[0] != "END":
    type_command, row, col, num = [int(el) if el.isdigit() else el for el in command]

    if not (0 <= row < size and 0 < col < size):
        print("Invalid coordinates")

    elif type_command == "Add":
        matrix[row][col] += num

    elif type_command == "Subtract":
        matrix[row][col] -= num

    command = input().split()

[print(*row) for row in matrix]
