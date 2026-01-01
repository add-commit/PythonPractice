import random
choices = ["rock", "paper", "scissor"]


while True:
    computers_choice = random.choice(choices)
    #print(computers_choice)
    user_choice = input("What is your choice :: ").lower()

    if user_choice not in choices:
        print("please enter rock or paper or scissor only")
    if user_choice == "quit":
        break
    if user_choice == computers_choice:
        print (f"its a tie, computers choice was {computers_choice}")
    elif (computers_choice=="rock" and user_choice=="paper") or  (computers_choice=="paper" and user_choice=="scissor") or (computers_choice=="scissor" and user_choice=="rock"):
        print (f"you won, computers choice was {computers_choice}")
    else:
        print(f"you lose, computers choice was {computers_choice}")