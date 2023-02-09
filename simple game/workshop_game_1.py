def check_for_win():
    player_name, player_symbol = players[0]

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(size)])
    second_diagonal_win = all([board[i][size - 1 - i] == player_symbol for i in range(size)])

    row_win = all([(pos == player_symbol for pos in row) for row in board])
    col_win = any([all(board[r][c] == player_symbol for r in range(size)) for c in range(size)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(f"{player_name} won!")

        exit()

    players.append(players.popleft())


def place_symbol(position):
    row, col = (position - 1) // size, (position - 1) % size

    board[row][col] = players[0][1]

    check_for_win()
    print_board()
    choose_position()


def choose_position():
    while True:
        try:
            position = int(input(f"{players[0][0]} choose a free position [1-9]"))
        except ValueError:
            print(f"{players[0][0]} enter valid position!")
            continue
        if 1 <= position <= size * size:
            place_symbol(position)
            break
        else:
            print(f"{players[0][0]} enter valid position!")


def print_board(begin=False):
    if begin:
        print("This is numeration of the board: ")
        [print(f"| {' | '.join(row)} |") for row in board]
        print(f"{players[0][0]} starts first!")

        for row in range(size):
            for col in range(size):
                board[row][col] = " "
    else:
        [print(f"| {' | '.join(row)} |") for row in board]


def start():
    player_one_name = input("PLayer one enter your name: ")
    player_two_name = input("PLayer two enter your name: ")

    while True:
        player_one_symbol = input(f"{player_one_name} would you like to play with 'X' ot 'O'?").upper()

        if player_one_symbol not in ["X", "O"]:
            print(f"{player_two_name} select a valid option!")
        else:
            break

    player_two_symbol = "O" if player_one_symbol == "X" else "X"

    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])

    print_board(begin=True)


players = []
board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, 10, 3)]
size = len(board)

start()
