import random

def print_board(board):
    print("Текущая доска:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def player_move(board, current_player):
    while True:
        try:
            row = int(input(f"Игрок {current_player}, введите номер строки (0-2): "))
            col = int(input(f"Игрок {current_player}, введите номер столбца (0-2): "))
            if board[row][col] == " ":
                board[row][col] = current_player
                break
            else:
                print("Эта клетка занята! Попробуйте снова.")
        except (ValueError, IndexError):
            print("Неверный ввод! Пожалуйста, введите числа от 0 до 2.")


def computer_move(board, current_player):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    row, col = random.choice(empty_cells)
    board[row][col] = current_player
    print(f"Компьютер (Игрок {current_player}) выбрал клетку: {row}, {col}")


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    mode = input("Выберите режим: 1 - Игрок против Игрока, 2 - Игрок против Компьютера: ")
    current_player = "X"

    while True:
        print_board(board)

        if mode == "1":
            player_move(board, current_player)
        else:
            if current_player == "X":
                player_move(board, current_player)
            else:
                computer_move(board, current_player)

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Игрок {winner} выиграл!")
            break

        if is_board_full(board):
            print_board(board)
            print("Игра закончилась вничью!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()