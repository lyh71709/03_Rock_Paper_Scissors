# RPS Component 1 - Get the user input

valid = False

while valid == False:
    chosen_action = input("What are you going to do? (Rock, Paper or Scissors)? ").lower()

    if chosen_action == "rock" or chosen_action == "r":
        print("You chose Rock")
        valid = True

    elif chosen_action == "paper" or chosen_action == "p":
        print("You chose Paper")
        valid = True

    elif chosen_action == "scissors" or chosen_action == "s":
        print("You chose Scissors")
        valid = True

    else:
        print("Please enter either Rock, Paper or Scissors")
        print()
