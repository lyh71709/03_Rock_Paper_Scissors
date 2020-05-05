# RPS Component 3 - Compare the user's action to the computer's randomly generated action and see if the user won or not
# V2 - assigns the outcome as a numeric value which is modified by the actions of the player and the cpu, this is to see if it is more efficient than writing a lot of if statements

valid = False
action = ["rock", "paper", "scissors"]

while valid == False:
    chosen_action = input("What are you going to do (Rock/Paper/Scissors)? ").lower()
    cpu_action = "rock"
    game_outcome = 0

    # Assign modifiers to actions
    if chosen_action == "rock":
        game_outcome += 3
    elif chosen_action == "paper":
        game_outcome += 2
    elif chosen_action == "scissors":
        game_outcome += 1
    else:
        print("Please enter either Rock, Paper or Scissors")
        print()
        continue

    # assign modifiers to CPU actions
    if cpu_action == "rock":
        game_outcome -= 3
    elif cpu_action == "paper":
        game_outcome -= 2
    else:
        game_outcome -= 1

    # set game outcomes
    if game_outcome == 0:
        print("The computer used {}".format(cpu_action))
        print("It was a draw")
    elif game_outcome == 1 or game_outcome == -2:
        print("The computer used {}".format(cpu_action))
        print("Sorry you lost")
    else:
        print("The computer used {}".format(cpu_action))
        print("You Won!!!")

    valid = True
