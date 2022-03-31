import random

score = [0, 0]
result = ""
possible_actions = ["rock", "paper", "scissor"]


def score_board(score, computer_action, user_choice, result):
    print(f""" 
    -----------------------------------
            {result}

    Computer used {computer_action} against your {user_choice}

    Your points: {score[0]}
    Computer points: {score[1]}
    -----------------------------------""")

 # ==================================
user_name = input("Please enter your player nickname: ")
print(f"Hello {user_name}, let's play! \n")
b = ["rock", "rok", "ock"]
while True:

    computer_action = random.choice(possible_actions)
    user_choice = input("Enter a choice rock, paper or scissor: ").lower()

    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissor":
        print("""

        Wrong option my friend!! U can use only rock, paper or scissor
        
        """)
    else:
        if user_choice == computer_action:
            result = "This is a tie"
            score[0] += 1
            score[1] += 1
        elif user_choice == "rock":
            if computer_action == "scissor":
                score[0] += 1
                result = "You win!"
            else:
                score[1] += 1
                result = "You lose! Try again!"
        elif user_choice == "paper":
            if computer_action == "rock":
                score[0] += 1
                result = "You win!"
            else:
                score[1] += 1
                result = "You lose! Try again!"
        elif user_choice == "scissor":
            if computer_action == "paper":
                score[0] += 1
                result = "You win!"
            else:
                score[1] += 1
                result = "You lose! Try again!"
        score_board(score, computer_action, user_choice, result)
    play_again = input(f"""                 {user_name}
    If u want countinue press: C
    If u want reset your score press: R
    If u want exit, press any button 
    -----------------------------------
    Your answer: """).lower()
    print()
    if play_again == "1":
        score = [0, 0]
    elif play_again != "c" and play_again != "r":
        print(f"""
        Your points: {score[0]}
        Computer points: {score[1]}
        Have a good day 😎✋""")
        break


# def losowoc
#   elif user_choice == "rock":
#             if computer_action == "scissor":
#                 score[0] += 1
#                 result = "You win!"
#             else:
#                 score[1] += 1
#                 result = "You lose! Try again!"
