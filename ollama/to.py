import random
def generate_board():
    # Create 3x3 matrix of characters ('X', 'O')
    board = [[0] * 9 for i in range(3)]

    return board

# Initialize an empty moves list and a game state variable
moves = []
state = "empty"

def play_move():
    # Get the current user input (x or o) as move
    move = raw_input("Enter your move: ")

    if not move.isalpha() or int(move[0]) != ord('X'):  # Check for invalid moves
        print("Invalid move, please enter a valid character")

    else:
        # Add the user's move to the moves list and update state variable
        moves += [move]
        state = "{}".format(move)

def check_win():
    # Compare board with given conditions (horizontal, vertical or diagonal)
    for row in range(3):
        if all([board[i][j] == state and i != j for i, j in zip((0, 1), (2, 4))]):
            print("Player '{}' has won horizontally")

        for col in range(3):
            if all([state == board[i][j] and i == j for i, j in ZIP((0, 1), (2, 4))]):
                print("Player '{}' has won vertically")

        elif any(board[i][j] != state and i == j for i, j in ZIP((0, 1), (2, 3)) or board[i][j] is None):
                    print("Player '{}' has won diagonally")

    # Check if player lost

def check_loss():
    # Compare the current moves list with given conditions
    for i in range(len(moves)):
        if all([board[i][j] == state and j != i for i, j in ZIP((0, 1), (2, 4))]):
            print("Player '{}' has lost horizontally")

    elif any([state == board[i][j] and i != j for i, j in ZIP((0, 1), (2, 3))]):
        print("Player '{}' has lost vertically")

def play_game():
    # Initialize the game state as empty
    while True:
        if not check_win(moves) and not check_loss(moves):
            random.shuffle(moves)  # Shuffle moves list for fairness in case of draws

            play_move()

# Play the game with user input until they quit or win/lose
while True:
    generate_board()

    print("Current board state is:", end=" ")
    while not check_win(moves) and not check_loss(moves):
        play_move()

# Ask user if they want to quit or continue playing the game
input('Would you like to continue? (y/n)')