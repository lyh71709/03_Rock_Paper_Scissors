# RPS Component 9 - Implementing Rock, Paper, Scissors, Lizard, Spock
# For this I think the method of comparisons v2 is better for this than writing a bunch of if statements
# Give users an option at the beginning of the game to either play RPS or RPSLS

def intcheck(question):
    while True:
        try:
            response = int(input(question))

            return response

        except ValueError:
            print("Please enter an integer, and remember it needs to be odd.")
            print()
            continue

valid2 = False
while valid2 == False:
    games_play = int(input("How many games would you like to play? (Put 1 for Round play and 2 for Continuous Play) "))

    if games_play == 1:
        games_number = int(input("How many games do you want to play? "))
        valid2 = True
        print()
    elif games_play > 2:
        print("Please enter either one for Round Play or two for Continuous Play ")
        continue
    else:
        valid2 = True

print()
games_played = 0
keep_going = ""
while keep_going == "":
    round_continue = "yes"
    cpu_score = 0
    user_score = 0

    print("Game {}".format(games_played + 1))

    rounds = intcheck("The game will be best out of what (Must be an odd number)? ")
    win = ((rounds//2)+1)
    print("You need {} wins to win".format(win))
    print()

    while round_continue == "yes":

        if cpu_score == win:
            print("Sorry the computer won")
            print()
            round_continue = "no"

        elif user_score == win:
            print("You beat the computer!!!")
            print()
            round_continue = "no"

        else:
            if (rounds % 2) == 1:
                rounds_played = 0

                while cpu_score != win and user_score != win:

                    print("Round {}".format(rounds_played + 1))

                    valid = False
                    action = ["rock", "paper", "scissors", "lizard", "spock"]

                    while valid == False:
                        chosen_action = input("What are you going to do (Rock/Paper/Scissors/Lizard/Spock)? ").lower()
                        cpu_action = "rock"
                        game_outcome = 0

                        if chosen_action == "rock":
                            game_outcome += 3
                        elif chosen_action == "paper":
                            game_outcome += 2
                        elif chosen_action == "scissors":
                            game_outcome += 1
                        elif chosen_action == "lizard":
                            game_outcome += 4
                        elif chosen_action == "spock":
                            game_outcome += 5
                        else:
                            print("Please enter either Rock, Paper or Scissors")
                            print()
                            continue

                        if cpu_action == "rock":
                            game_outcome -= 3
                        elif cpu_action == "paper":
                            game_outcome -= 2
                        elif cpu_action == "scissors":
                            game_outcome -= 1
                        elif cpu_action == "lizard":
                            game_outcome -= 4
                        else:
                            game_outcome -= 5

                        if game_outcome == 0:
                            print("The computer used {}".format(cpu_action))
                            print("It was a draw")
                        elif game_outcome == 1 or game_outcome == -2 or game_outcome == -4 or game_outcome == 3:
                            print("The computer used {}".format(cpu_action))
                            print("Sorry you lost")
                            cpu_score += 1
                        else:
                            print("The computer used {}".format(cpu_action))
                            print("You Won!!!")
                            user_score += 1

                        valid = True

                        print()
            else:
                print("Please enter an odd number as to ensure no ties")
                print()

    games_played += 1

    if games_play == 2:
        keep_going = input("Press <enter> to play again or any key to quit ")
    elif games_play == 1:
        if games_played == games_number:
            print("Thanks for playing")
            keep_going = "stop"

