import random
game_count= 0
while True:
    print("Hello ! Today we will play in Guessing Number game !")
    user_Number = int(input("Please enter your number here: "))
    gNumber = random.randint(1, 9)
    if user_Number  == gNumber:
        print('You guessed number right !')
    elif user_Number < gNumber:
        print('You guessed too low !')
    else:
        print('You guessed too high !')

    game_count += 1
    play_Again = input("Do you want to play again ? (yes/no): ").strip().lower()
    if play_Again == "yes":
        continue
    else:
        print(f"You played total " + str(game_count) + "  games, Thank you for playing our game !")
        break
