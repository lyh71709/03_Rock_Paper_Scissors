# RPS Component 8 - Loop Mechanics

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

how_many_games = input("How many games would you like to play? (There is also a continuous play mode where you keep on playing until whenever you want, just enter 'continuous') ")

if how_many_games == "continuous":
    

rounds = intcheck("The game will be best out of what (Must be an odd number)? ")
win = ((rounds//2)+1)
print("You need {} wins to win".format(win))

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
                action = ["rock", "paper", "scissors"]

                while valid == False:
                    chosen_action = input("What are you going to do (Rock/Paper/Scissors)? ").lower()
                    cpu_action = "rock"
                    game_outcome = 0

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

                    if cpu_action == "rock":
                        game_outcome -= 3
                    elif cpu_action == "paper":
                        game_outcome -= 2
                    else:
                        game_outcome -= 1

                    if game_outcome == 0:
                        print("The computer used {}".format(cpu_action))
                        print("It was a draw")
                    elif game_outcome == 1 or game_outcome == -2:
                        print("The computer used {}".format(cpu_action))
                        print("Sorry you lost")
                        cpu_score += 1
                    else:
                        print("The computer used {}".format(cpu_action))
                        print("You Won!!!")
                        user_score += 1

                    valid = True

                    print()
                    rounds_played += 1
        else:
            print("Please enter an odd number as to ensure no ties")
            print()

