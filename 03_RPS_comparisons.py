# RPS Component 3 - Compare the user's action to the computer's randomly generated action and see if the user won or not

valid = False
action = ["Rock", "Paper", "Scissors"]

while valid == False:
    chosen_action = input("What are you going to do (Rock/Paper/Scissors)? ").lower()
    cpu_action = "rock"

    if chosen_action == "rock":

        if cpu_action == "rock":
            print("The computer used Rock")
            print("It was a draw")

        elif cpu_action == "paper":
            print("The computer used Paper")
            print("Sorry you lost")

        else:
            print("The computer used Scissors")
            print("You Won!")

        valid = True

    elif chosen_action == "paper":

        if cpu_action == "rock":
            print("The computer used Rock")
            print("You Won!")

        elif cpu_action == "paper":
            print("The computer used Paper")
            print("It was a draw")

        else:
            print("The computer used Scissors")
            print("Sorry you lost")

        valid = True

    elif chosen_action == "scissors":

        if cpu_action == "rock":
            print("The computer used Rock")
            print("Sorry you lost")

        elif cpu_action == "paper":
            print("The computer used Paper")
            print("You Win!")

        else:
            print("The computer used Scissors")
            print("It was a draw")

        valid = True

    else:
        print("Please enter either Rock, Paper or Scissors")

    print()
