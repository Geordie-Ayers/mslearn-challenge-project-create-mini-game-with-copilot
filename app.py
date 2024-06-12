import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_wins = 0
    computer_wins = 0

    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()

        if user_choice == 'q':
            break

        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}\n")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            user_wins += 1
        else:
            print("You lose!")
            computer_wins += 1

        print(f"\nRounds won by you: {user_wins}")
        print(f"Rounds won by computer: {computer_wins}\n")

play_game()
