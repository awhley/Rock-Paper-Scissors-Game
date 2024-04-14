import random

print("\n\tWelcome to Rock-Paper-Scissors!")

CHOICES = ("rock", "paper", "scissors")
WIN_MESSAGES = {
    "rock": {"paper": "Paper covers rock! You lose.", "scissors": "Rock smashes scissors! You win!"},
    "paper": {"rock": "Paper covers rock! You win!", "scissors": "Scissors cut paper! You lose."},
    "scissors": {"rock": "Rock crushes scissors! You lose.", "paper": "Scissors cut paper! You win!"}
}
TIE_MESSAGE = "It's a tie!"

def get_computer_choice():
    return random.choice(CHOICES)

def get_user_choice():
    while True:
        choice = input("\nYour Choice: ").lower()
        if choice in CHOICES:
            return choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    WINS = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }
    if WINS[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"

def display_result(winner, user_choice, computer_choice):
    if winner == "user":
        print(f"Computer Choice: {computer_choice}\n")
        print(f"{WIN_MESSAGES[user_choice][computer_choice]}\n")
    elif user_choice == computer_choice:
        print(f"Computer Choice: {computer_choice}\n")
        print(f"{TIE_MESSAGE}\n")    
    else:
        print(f"Computer Choice: {computer_choice}\n")
        print(f"{(WIN_MESSAGES[user_choice][computer_choice])}\nTry again!\n")

def main():
    playing = True
    while playing:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(winner, user_choice, computer_choice)

        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            print("\n Thanks for playing!\n")
            playing = False
        
if __name__ == "__main__":
    main()