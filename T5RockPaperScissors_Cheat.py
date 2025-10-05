import random

# Function to get the computer's choice
def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)
# Function to get the player's choice

def get_player_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return choice

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"
    
# Main game function
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    computer_choice = get_computer_choice()
    print(computer_choice)
    player_choice = get_player_choice()
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    # Determine and display the winner
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Call the main game function to start the game
play_game()
