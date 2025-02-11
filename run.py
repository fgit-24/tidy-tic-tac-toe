import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# High-level overview

# Display
# render_display: Function to show the current state of the game board.

# Game Dynamics
# start_game: Main function to initiate and control the flow of the game.
# process_turn: Manage each player's turn.
# determine_if_game_finished: Determine if the game has ended.
# find_winner: Check if there is a winner.
# evaluate_rows: Check rows for a win.
# evaluate_columns: Check columns for a win.
# evaluate_diagonals: Check diagonals for a win.
# detect_tie: Check if the game is a tie.
# switch_player: Switch the current player.


# ----- Global Variables Start -----

# Game board represented as a list of 9 elements
game_board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

# Boolean to track if the game is still in progress
game_in_progress = True

# Variable to store the winner (either 'X' or 'O') or None if no winner
game_winner = None

# Variable to keep track of the current player ('X' or 'O')
active_player = "X"

# ----- Global Variables End -----


def welcome_text_one():
    clear()
    print("Hey internet-traveler, it's great to have you!\n")
    print("Here you can experience an epic one-on-one tic tac toe battle ")
    print("with, or against, your partner or friend!\n")
    print("")
    print("This game is designed to help you ")
    print("with the great decisions in life!")
    print("")
    print("- You don't know where to book the next vacation?")
    print("  The winner decides!")
    print("")
    print("- You don't know what to have for dinner?")
    print("It's up to the winner to decide!")
    print("")
    print("- You are not sure if you want to marry or not?")
    print("Well, you know now how it works!")
    print("")
    input("\nPress ENTER to continue\n")

    welcome_text_two()


def welcome_text_two():
    clear()
    print("Enjoy this epic game, share it everywhere, ")
    print("and most importantly, have fun!")
    print("")
    print("In addition, feel free to visit my profile on")
    print("")
    print("    [Snipverse.com](https://snipverse.com/fhaas)")
    print("and follow me on")
    print("    [LinkedIn](https://www.linkedin.com/in/-florian-haas-)!")
    print("")
    print("See you at my next awesome project!")
    input("\nPress ENTER to continue\n")

    # Continue with instructions
    instructions()


def instructions():
    clear()
    print("Instructions:")
    print("")
    print("1. The game board is a 3x3 grid with cells numbered 1 to 9:")
    print("")
    print("    1 | 2 | 3")
    print("   ---|---|---")
    print("    4 | 5 | 6")
    print("   ---|---|---")
    print("    7 | 8 | 9")
    print("")
    print("2. Players take turns to place their marks (X or O) on the board.")
    print("")
    print("3. Enter the cell number where you want to place your mark.")
    print("")
    print("4. Type 'reset' at any time to restart the game.")
    print("")
    print("5. The first player to get three in a row wins.")
    print("   If the board is full and no one has three in a row, ")
    print("   it's a draw.")
    print("")
    print("Enjoy the game!")
    input("\nPress ENTER to continue\n")

    # Start the game
    start_game()


# Function to display the current state of the game board
def render_display():
    for i in range(0, 9, 3):
        print('|'.join(game_board[i:i+3]))
    print()


# Function to reset the game state
def reset_game():
    global game_board, game_in_progress, game_winner, active_player
    game_board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    game_in_progress = True
    game_winner = None
    active_player = "X"
    print("The game has been reset!")
    # Show the empty board after reset
    render_display()


# Clear function to clean-up the terminal so things don't get messy.
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Main function to start and control the flow of the game
def start_game():
    global game_in_progress, game_winner
    clear()

    # Display the initial empty board
    render_display()

    # Keep the game running indefinitely until user decides to restart
    while True:
        if not game_in_progress:  # If game is over, prompt for a reset
            choice = input("Game over. Type 'reset' to start a new game: ")
            clear()
            choice = choice.strip().lower()
            if choice == 'reset':
                reset_game()
                continue
            else:
                print(f"{choice} is an invalid input.")
                print("Type 'reset' to start a new game.")
                continue

        # Handle the turn of the current player
        process_turn(active_player)

        # Check if the game has been won or is a tie
        determine_if_game_finished()

        # The game has ended
        if game_winner:
            print(Fore.GREEN + f"{game_winner} won!")
            game_in_progress = False
        elif not game_in_progress and game_winner is None:
            print("It's a tie!")

        # Switch to the other player
        switch_player()


# Handle a single turn for the given player
def process_turn(player):
    global game_board
    valid_move = False
    clear()
    while not valid_move:
        print(f"{player}'s turn!")
        render_display()

        prompt = "Choose a position from 1 to 9 or type 'reset' to restart: "
        raw_input = input(prompt)
        stripped_input = raw_input.strip()
        position = stripped_input.lower()
        clear()

        # Check if the user wants to reset the game
        if position == 'reset':
            clear()
            reset_game()
            return

        # Ensure the player inputs a valid number
        if not position.isdigit():
            render_display()
            print(Fore.RED + f"{position} is an invalid input. "
                  "Please enter a number from 1 to 9.")
            input('Press enter to continue.')
            clear()
            continue

        position = int(position) - 1

        # Check if position is valid and available
        if 0 <= position < 9:
            if game_board[position] == "-":
                valid_move = True
            else:
                render_display()
                print(Fore.RED + 'You can\'t go there, go again!')
                input('Press enter to continue.')
                clear()
        else:
            render_display()
            print(Fore.RED + f"{position + 1} is an invalid position. "
                             "Please choose a number "
                             "from 1 to 9.")
            input('Press enter to continue.')
            clear()

    clear()
    # Place the player's marker on the board
    game_board[position] = player
    # Display the updated board
    render_display()


# Check if the game is over due to a win or tie
def determine_if_game_finished():
    find_winner()
    detect_tie()


# Determine if there is a winner
def find_winner():
    global game_winner

    # Check for a win in rows, columns, and diagonals
    row_victory = evaluate_rows()
    column_victory = evaluate_columns()
    diagonal_victory = evaluate_diagonals()

    # Set the winner if there is one
    if row_victory:
        game_winner = row_victory
    elif column_victory:
        game_winner = column_victory
    elif diagonal_victory:
        game_winner = diagonal_victory


# Check if any row has all the same value and is not empty
def evaluate_rows():
    global game_in_progress

    rows = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    for row in rows:
        mark1 = game_board[row[0]]
        mark2 = game_board[row[1]]
        mark3 = game_board[row[2]]

        if mark1 == mark2 == mark3 and mark1 != '-':
            game_in_progress = False
            return mark1
    return None


# Check if any column has all the same value and is not empty
def evaluate_columns():
    global game_in_progress

    columns = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
    for col in columns:
        value1 = game_board[col[0]]
        value2 = game_board[col[1]]
        value3 = game_board[col[2]]

    # Check if all three values are the same and not '-'
        if value1 == value2 == value3 and value1 != '-':
            game_in_progress = False
            return value1
    return None


# Check if any diagonal has all the same value and is not empty
def evaluate_diagonals():
    global game_in_progress

    diagonals = [(0, 4, 8), (2, 4, 6)]
    for diag in diagonals:
        mark1 = game_board[diag[0]]
        mark2 = game_board[diag[1]]
        mark3 = game_board[diag[2]]

        # Ensure the marks are the same and not '-'
        if mark1 == mark2 == mark3 and mark1 != '-':
            game_in_progress = False
            return mark1
    return None


# Checks if there is a tie
def detect_tie():
    global game_in_progress
    if "-" not in game_board:
        game_in_progress = False


# Flips player, after players turn
def switch_player():
    global active_player
    active_player = 'O' if active_player == 'X' else 'X'


if __name__ == "__main__":
    clear()
    welcome_text_one()
