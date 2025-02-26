import random

total_guesses = 0

while True:
    print("Hello! Let's play the Guessing Number game!")
    number = random.randint(1, 9)

    user_input = input("Guess a number between 1 and 9 (or 'exit' to quit): ").strip().lower()

    if user_input == 'exit':
        break

    try:
        user_number = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number or 'exit'.")
        continue

    total_guesses += 1

    if user_number == number:
        print("Congratulations! You guessed it right!")
    elif user_number < number:
        print("Too low!")
    else:
        print("Too high!")

    play_again = input("Do you want to play again? (yes/no or 'exit'): ").strip().lower()
    if play_again in ['no', 'exit']:
        break

print(f"Total guesses: {total_guesses}. Thank you for playing!")