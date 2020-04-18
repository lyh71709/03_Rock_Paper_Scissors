# RPS Component 5 - Win / Loss Mechanics

def intcheck(question):
    while True:
        try:
            response = int(input(question))

            return response

        except ValueError:
            print("Please enter an integer, and remember it needs to be odd.")
            print()
            continue

round_continue = "yes"
cpu_score = 0
user_score = 0

rounds = intcheck("The game will be best out of what (Must be an odd number)? ")
win = ((rounds//2)+1)

while round_continue == "yes":

    if cpu_score == win:
        print("Sorry the computer won")
        print("You have gotten to the end of the game")
        round_continue = "no"

    elif user_score == win:
        print("You beat the computer!!!")
        print("You have gotten to the end of the game")
        round_continue = "no"

    else:
        if (rounds % 2) == 1:
            rounds_played = 0

            while cpu_score != win and user_score != win:

                print("Round {}".format(rounds_played + 1))

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
                            cpu_score += 1

                        else:
                            print("The computer used Scissors")
                            print("You Won!")
                            user_score += 1

                        valid = True

                    elif chosen_action == "paper":

                        if cpu_action == "rock":
                            print("The computer used Rock")
                            print("You Won!")
                            user_score += 1

                        elif cpu_action == "paper":
                            print("The computer used Paper")
                            print("It was a draw")

                        else:
                            print("The computer used Scissors")
                            print("Sorry you lost")
                            cpu_score += 1

                        valid = True

                    elif chosen_action == "scissors":

                        if cpu_action == "rock":
                            print("The computer used Rock")
                            print("Sorry you lost")
                            cpu_score += 1

                        elif cpu_action == "paper":
                            print("The computer used Paper")
                            print("You Win!")
                            user_score += 1

                        else:
                            print("The computer used Scissors")
                            print("It was a draw")

                        valid = True

                    else:
                        print("Please enter either Rock, Paper or Scissors")

                    print()
                    rounds_played += 1

        else:
            print("Please enter an odd number as to ensure no ties")
            print()
