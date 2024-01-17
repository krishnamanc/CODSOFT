import math
import random

BOARD_SIZE = 9
EMPTY_CELL = '-'
AI_SYMBOL = 'O'
PLAYER_SYMBOL = 'X'


def display_board(board):
    """Display the tic-tac-toe board."""
    for i in range(0, BOARD_SIZE, 3):
        print(board[i] + '|' + board[i + 1] + '|' + board[i + 2])
        if i < BOARD_SIZE - 3:
            print('-+-+-')
    print()


def display_positions():
    """Display the positions (0-8) beside the tic-tac-toe board."""
    positions_board = [str(i) for i in range(BOARD_SIZE)]
    for i in range(0, BOARD_SIZE, 3):
        print(positions_board[i] + '|' + positions_board[i + 1] + '|' + positions_board[i + 2])
        if i < BOARD_SIZE - 3:
            print('-+-+-')
    print()


def check_winner(board, player):
    """Check if a player has won the game."""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_board_full(board):
    """Check if the board is full."""
    return all(cell != EMPTY_CELL for cell in board)


def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    """Minimax algorithm with alpha-beta pruning."""
    if check_winner(board, AI_SYMBOL):
        return 1
    elif check_winner(board, PLAYER_SYMBOL):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(BOARD_SIZE):
            if board[i] == EMPTY_CELL:
                board[i] = AI_SYMBOL
                eval = minimax_alpha_beta(board, depth + 1, alpha, beta, False)
                board[i] = EMPTY_CELL
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(BOARD_SIZE):
            if board[i] == EMPTY_CELL:
                board[i] = PLAYER_SYMBOL
                eval = minimax_alpha_beta(board, depth + 1, alpha, beta, True)
                board[i] = EMPTY_CELL
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval


def find_best_move(board):
    """Find the best move for the AI."""
    best_moves = []
    best_eval = -math.inf
    for i in range(BOARD_SIZE):
        if board[i] == EMPTY_CELL:
            board[i] = AI_SYMBOL
            eval = minimax_alpha_beta(board, 0, -math.inf, math.inf, False)
            board[i] = EMPTY_CELL
            if eval > best_eval:
                best_eval = eval
                best_moves = [i]
            elif eval == best_eval:
                best_moves.append(i)
    return random.choice(best_moves) if best_moves else -1


def play_again():
    """Ask the user if they want to play again."""
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')


# Main game loop
while True:
    board = [EMPTY_CELL] * BOARD_SIZE
    print("Welcome to Tic-Tac-Toe!")

    while True:
        display_positions()
        display_board(board)
        
        move = int(input("Select your move (0-8): "))

        if 0 <= move < BOARD_SIZE and board[move] == EMPTY_CELL:
            board[move] = PLAYER_SYMBOL

            if check_winner(board, PLAYER_SYMBOL):
                display_positions()
                display_board(board)
                print("Congratulations! You win!")
                break
            elif is_board_full(board):
                display_positions()
                display_board(board)
                print("It's a draw!")
                break

            ai_move = find_best_move(board)
            board[ai_move] = AI_SYMBOL

            if check_winner(board, AI_SYMBOL):
                display_positions()
                display_board(board)
                print("AI wins! Better luck next time.")
                break
            elif is_board_full(board):
                display_positions()
                display_board(board)
                print("It's a draw!")
                break
        else:
            print("Invalid move. Please try again.")

    if not play_again():
        print("Thanks for playing! Goodbye.")
        break
