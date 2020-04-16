# RPS Component 1 - Get the user input

valid = False

while valid == False:
    chosen_attack = input("What are you going to do? (Rock, Paper or Scissors)? ").lower()

    if chosen_attack == "rock" or chosen_attack == "r":
        print("You chose Rock")
        valid = True

    elif chosen_attack == "paper" or chosen_attack == "p":
        print("You chose Paper")
        valid = True

    elif chosen_attack == "scissors" or chosen_attack == "s":
        print("You chose Scissors")
        valid = True

    else:
        print("Please enter either Rock, Paper or Scissors")
        print()
