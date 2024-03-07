
# Purpose of the game:The game aims to create a competition between two players by each of them choosing numbers from a list
# containing numbers from 1 to 9, so that if any of the players is able to choose three numbers whose sum equals 15,
# he is declared the winner of the game and the game is over. However, if both of them are unable to choose Numbers
# including three numbers whose sum equals 15 are declared a tie, i.e. none of them win

# Function to introduce the game rules
def introduction_game():
    print("Welcome to our game!")
    print("The game requires two players.")
    print("Each player should choose a number between 1 and 9.")
    print("The player who reaches the sum of 15 first wins, and the game ends.")
    print("If both players don't reach the sum of 15, it's a draw, and the game ends.")

# Call the introduction function to display game rules
introduction_game()

# Prompt to start the game
game_start = input("If you want to start, write enter: ")
print()

# Function to check if a player has won by reaching the sum of 15
def check_win(player_numbers):
    if len(player_numbers) < 3:
        return False
    else:
        for m in range(len(player_numbers)):
            for n in range(m + 1, len(player_numbers)):
                for k in range(n + 1, len(player_numbers)):
                    if player_numbers[m] + player_numbers[n] + player_numbers[k] == 15:
                        return True
    return False

# Function to manage the main game logic
def number_scrabble():
    # Initialize the list of available numbers
    game_list = list(range(1, 10))  # 1 to 9
    player1_numbers = []  # List to store player 1's chosen numbers
    player2_numbers = []  # List to store player 2's chosen numbers

    # Loop until the game list is empty
    while game_list:
        # Player 1's turn
        print("Available numbers are:", game_list)
        try:
            player1_choice = int(input("Player 1, choose a valid number: "))
            if player1_choice not in game_list:
                raise ValueError("Invalid choice. Choose a valid number from the available list.")
        except ValueError as e:
            print(e)
            continue

        # Update game list and player 1's numbers
        game_list.remove(player1_choice)
        player1_numbers.append(player1_choice)

        # Check for a draw
        if not game_list:
            print("It's a draw!")
            return

        # Player 2's turn
        print("Available numbers:", game_list)
        try:
            player2_choice = int(input("Player 2, choose a number: "))
            if player2_choice not in game_list:
                raise ValueError("Invalid choice. Choose a number from the available list.")
        except ValueError as e:
            print(e)
            continue

        # Update game list and player 2's numbers
        game_list.remove(player2_choice)
        player2_numbers.append(player2_choice)

        # Check if player 1 has won
        if check_win(player1_numbers):
            print("Player 1 wins!")
            return

        # Check if player 2 has won
        if check_win(player2_numbers):
            print("Player 2 wins!")
            return

# Call the function
number_scrabble()