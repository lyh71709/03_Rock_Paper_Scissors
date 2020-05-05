# RPS Component 9 - Make a way for the user to switch between RPS and RPSLS
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

# Have a way to switch between RPS and RPSLS
valid3 = False
while valid3 == False:
    game_mode = input("What gamemode would you like to play? (RPS or RPSLS) ").upper()
    if game_mode == "RPS":
        print("You are playing Rock, Paper, Scissors")
        valid3 = True
    elif game_mode == "RPSLS":
        print("You are playing Rock, Paper, Scissors, Lizard, Spock")
        valid3 = True
    else:
        print("Please enter either RPS or RPSLS")

game_summary = []
print()
valid2 = False
while valid2 == False:
    games_play = input("How many games would you like to play? (Round or Continuous Play) ").lower()

    if games_play == "round" or games_play == "r":
        games_number = intcheck("How many games do you want to play? ")
        valid2 = True
    elif games_play == "continuous" or games_play == "c":
        valid2 = True
    else:
        print("Please enter either round or continuous ")
        continue

games_played = 0
keep_going = ""
while keep_going == "":
    round_continue = "yes"
    cpu_score = 0
    user_score = 0
    print()
    print("Game {}".format(games_played + 1))

    # RPSLS Game function
    while round_continue == "yes":
        cpu_score = 0
        user_score = 0
        rounds = intcheck("The game will be best out of what (Must be an odd number)? ")
        win = ((rounds//2)+1)
        if (rounds % 2) == 1:
            rounds_played = 0
            print("You need {} wins to win".format(win))

            if game_mode == "RPSLS":
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
                            print("Please enter either Rock, Paper, Scissors, Lizard or Spock")
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
                        round_summary = None
                        rounds_played += 1
                        print()

                    if cpu_score == win:
                        print("Sorry the computer won")
                        print()
                        round_summary = "CPU Win"
                        round_continue = "no"
                    elif user_score == win:
                        print("You beat the computer!!!")
                        print()
                        round_summary = "User Win"
                        round_continue = "no"

                    if round_summary is not None:
                        game_summary.append(round_summary)

            # RPS Game function
            if game_mode == "RPS":
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
                            round_summary = None
                            rounds_played += 1
                            print()

                            if cpu_score == win:
                                print("Sorry the computer won")
                                print()
                                round_summary = "CPU Win"
                                round_continue = "no"
                            elif user_score == win:
                                print("You beat the computer!!!")
                                print()
                                round_summary = "User Win"
                                round_continue = "no"

                            if round_summary is not None:
                                game_summary.append(round_summary)
        else:
            print("Please enter an odd number as to ensure no ties")
            print()

    # End of gamemodes
    games_played += 1
    if games_play == "c" or games_play == "continuous":
        keep_going = input("Press <enter> to play again or any key to quit ")
    elif games_play == "r" or games_play == "round":
        if games_played == games_number:
            print("Thanks for playing")
            keep_going = "stop"

# Game Summary
print()
print("Outcome for Each Round")
list_count = 1
for item in game_summary:
    print("Round {}: {}".format(list_count, item))
    list_count += 1
