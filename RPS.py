import random

def get_game(user_input):
    computer_input = random.randint(1,3)
    computer_decision = ""
    if computer_input == 1:
        computer_decision = "Rock"
    elif computer_input == 2:
        computer_decision = "Paper"
    else:
        computer_decision = "Scissors"
    print(computer_decision)
    if computer_decision == user_input:
        print("Draw")
    elif computer_decision == "Rock" and user_input == "Paper":
        print("Player Won !")
    elif computer_decision == "Paper" and user_input == "Rock":
        print("Computer Won !")
    elif computer_decision == "Scissors" and user_input == "Rock":
        print("Player Won !")
    elif computer_decision == "Rock" and user_input =="Scissors":
        print("Computer Won !")
    elif computer_decision == "Paper" and user_input == "Scissors":
        print("Player Won !")
    else:
        print("Computer Won !")


print("Hello ! Today we will play in \"Rock, Paper, Scissors\" game !")
user_input = input("Please enter your figure here:")
get_game(user_input)