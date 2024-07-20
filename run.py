# High-level overview

# Display
## render_display: Function to show the current state of the game board.

# Game Dynamics
## start_game: Main function to initiate and control the flow of the game.
## process_turn: Manage each player's turn.
## determine_if_game_finished: Determine if the game has ended.
#### find_winner: Check if there is a winner.
##### evaluate_rows: Check rows for a win.
##### evaluate_columns: Check columns for a win.
##### evaluate_diagonals: Check diagonals for a win.
### detect_tie: Check if the game is a tie.
## switch_player: Switch the current player.



# ----- Global Variables Start -----



# Game board represented as a list of 9 elements
game_board = ['-', '-', '-',
              '-', '-', '-',
              '-', '-', '-']


# Boolean to track if the game is still in progress
game_in_progress = True

      
# Function to display the current state of the game board
def render_display():
    for i in range(0, 9, 3):
        print(game_board[i] + '|' + game_board[i+1] + '|' + game_board[i+2])
    print()


# Display the initial empty board
render_display()


# Variable to store the winner (either 'X' or 'O') or None if no winner
game_winner = None


# Variable to keep track of the current player ('X' or 'O')
active_player = "X"



# ----- Global Variables End -----



# Main function to start and control the flow of the game
def start_game():
    global game_in_progress, game_winner

    # Display the initial empty board
    # render_display()

    while game_in_progress:
        # Handle the turn of the current player
        process_turn(active_player)

        # Check if the game has been won or is a tie
        determine_if_game_finished()

        # The game has ended
        if game_winner:
            print(game_winner + ' won!')
            game_in_progress = False
        elif not game_in_progress and game_winner is None:
            print("It's a tie!")

        # Switch to the other player
        switch_player()

    #  Handle a single turn for the given player
    def process_turn(player):
        print(f"{player}'s turn!")
        
        valid_move = False
        while not valid_move:
            position = input("Choose a position from 1 to 9: ")

            # Ensure the player inputs a valid number
            if position not in [str(i) for i in range(1, 10)]:
                print("Invalid input. Please choose a valid position from 1 to 9.")
                continue
            
            position = int(position) - 1

            # Check if the chosen position is available
            if game_board[position] == "-":
                valid_move = True
            else:
                print('You can\'t go there, go again!')

        # Place the player's marker on the board
        game_board[position] = player
        # Display the updated board
        render_display()

# Flips player, after players turn
def switch_player():
    global active_player
    active_player = 'O' if active_player == 'X' else 'X'


# Start the game
start_game()