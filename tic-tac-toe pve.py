import random

board = [" " for i in range(9)]
winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def print_board():
    print("""
    {} | {} | {}
    ---------
    {} | {} | {}
    ---------
    {} | {} | {}
    """.format(*board))

def player_move(icon):
    while True:
        choice = int(input("Enter your move (1-9): ").strip()) - 1
        if board[choice] == " ":
            board[choice] = icon
            break
        print("That space is already taken!")

def ai_move(icon):
    global board

    # Check for a winning move
    for c in winning_combinations:
        count = 0
        for i in c:
            if board[i] == icon:
                count += 1
        if count == 2:
            for i in c:
                if board[i] == " ":
                    board[i] = icon
                    return

    # Check for a blocking move
    for c in winning_combinations:
        count = 0
        for i in c:
            if board[i] == player_icon:
                count += 1
        if count == 2:
            for i in c:
                if board[i] == " ":
                    board[i] = icon
                    return

    # Take a random move
    possible_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(possible_moves)
    board[move] = icon

player_icon = "X"
if random.randint(0, 1) == 0:
    player_icon = "O"

while True:
    print_board()
    if player_icon == "X":
        player_move("X")
    if any(all(board[i] == "X" for i in c) for c in winning_combinations):
        print_board()
        print("X wins! Congratulations!")
        break
    if not any(i for i in range(9) if board[i] == " "):
        print_board()
        print("It's a draw!")
        break
    ai_move("O")
    if any(all(board[i] == "O" for i in c) for c in winning_combinations):
        print_board()
        print("O wins! Congratulations!")
        break
