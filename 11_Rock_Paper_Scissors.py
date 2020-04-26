# RPS - Complete Game

print("Welcome to Rock, Paper, Scissors")
print("The rules of this game are simple")
print()
print("The game is basically Rock, Paper, Scissors, with a couple touches.\n"
      "The game will begin by asking you which gamemode you want to play. \n"
      "The gamemodes are RPS(Rock, Paper, Scissors) and RPSLS(Rock, Paper, Scissors,\n"
      "Lizard, Spock). Then the game will ask how many games you want to play, \n"
      "Rounds means that you will have a set amount of games to play to your choosing\n"
      "Continuous means that games will keep going until you decide when you want to stop.\n"
      "A couple things you should know putting the first letter of an action is fine\n"
      "For example for rock you can put in 'r' or for continuous you can put in c and so and so.\n"
      "")
rpsls_help = input("Do you want me to tell you how 'Rock, Paper, Scissors, Lizard, Spock' works (Yes or No)? ").lower()

if rpsls_help == "yes" or rpsls_help == "y":
      print()
      print("Well, Scissors cuts Paper,\n"
          "Paper covers Rock,\n"
          "Rock crushes Lizard,\n"
          "Lizard poisons Spock,\n"
          "Spock smashes Scissors,\n"
          "Scissors decapitates Lizard,\n"
          "Lizard eats Paper,\n"
          "Paper disproves Spock,\n"
          "Spock vaporizes Rock,\n"
          "and as it always has, Rock crushes Scissors,\n"
            "\n"
          "Now let the game begin!")

elif rpsls_help == "no" or rpsls_help == "n":
      print()
      print("OK then let the game begin!")
else:
      print()
      print("You didn't put yes so i'm gonna take it as a no,\n"
          "Now let the game begin!")

import random

def rps_statement1(statement, char):
    print()
    print(char*(len(statement)+12))
    print("{} \ {}  | {}".format(user_icon, cpu_icon, statement))
    print(char*(len(statement)+12))
    print()

def rps_statement2(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()

def intcheck(question):
    while True:
        try:
            response = int(input(question))

            return response

        except ValueError:
            print("Please enter an integer, and remember it needs to be odd.")
            print()
            continue

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

game_summary = []
games_played = 0
keep_going = ""
while keep_going == "":
    round_continue = "yes"
    cpu_score = 0
    user_score = 0
    print()
    game_start = rps_statement2("          Game {}   ".format(games_played + 1), "◾")

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
                    round_start = rps_statement2("         Round {}         ".format(rounds_played + 1), "=")
                    valid = False
                    action = ["rock", "paper", "scissors", "lizard", "spock"]

                    while valid == False:
                        chosen_action = input("What are you going to do (Rock/Paper/Scissors/Lizard/Spock)? ").lower()
                        cpu_action = random.choice(action)
                        game_outcome = 0

                        if chosen_action == "rock":
                            game_outcome += 3
                            user_icon = "🥔"
                        elif chosen_action == "paper":
                            game_outcome += 2
                            user_icon = "🧻"
                        elif chosen_action == "scissors":
                            game_outcome += 1
                            user_icon = "✂"
                        elif chosen_action == "lizard":
                            game_outcome += 4
                            user_icon = "🦎"
                        elif chosen_action == "spock":
                            game_outcome += 5
                            user_icon = "🖖"
                        else:
                            print("Please enter either Rock, Paper or Scissors")
                            print()
                            continue
                        print()

                        if cpu_action == "rock":
                            game_outcome -= 3
                            cpu_icon = "🥔"
                        elif cpu_action == "paper":
                            game_outcome -= 2
                            cpu_icon = "🧻"
                        elif cpu_action == "scissors":
                            game_outcome -= 1
                            cpu_icon = "✂"
                        elif cpu_action == "lizard":
                            game_outcome -= 4
                            cpu_icon = "🦎"
                        else:
                            game_outcome -= 5
                            cpu_icon = "🖖"

                        if game_outcome == 0:
                            print("The computer used {}".format(cpu_action))
                            draw = rps_statement1("It was a draw", "-")
                        elif game_outcome == 1 or game_outcome == -2 or game_outcome == -4 or game_outcome == 3:
                            print("The computer used {}".format(cpu_action))
                            lose = rps_statement1("Sorry you lost", "-")
                            cpu_score += 1
                        else:
                            print("The computer used {}".format(cpu_action))
                            win = rps_statement1("You Win!!!","-")
                            user_score += 1
                        valid = True
                        round_summary = None
                        rounds_played += 1

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

            if game_mode == "RPS":
                    while cpu_score != win and user_score != win:
                        print("Round {}".format(rounds_played + 1))
                        valid = False
                        action = ["rock", "paper", "scissors"]

                        while valid == False:
                            chosen_action = input("What are you going to do (Rock/Paper/Scissors)? ").lower()
                            cpu_action = random.choice(action)
                            game_outcome = 0

                            if chosen_action == "rock":
                                game_outcome += 3
                                user_icon = "🥔"
                            elif chosen_action == "paper":
                                game_outcome += 2
                                user_icon = "🧻"
                            elif chosen_action == "scissors":
                                game_outcome += 1
                                user_icon = "✂"
                            else:
                                print("Please enter either Rock, Paper or Scissors")
                                print()
                                continue

                            if cpu_action == "rock":
                                game_outcome -= 3
                                cpu_icon = "🥔"
                            elif cpu_action == "paper":
                                game_outcome -= 2
                                cpu_icon = "🧻"
                            else:
                                game_outcome -= 1
                                cpu_icon = "✂"

                            if game_outcome == 0:
                                print("The computer used {}".format(cpu_action))
                                draw = rps_statement1("It was a draw", "-")
                            elif game_outcome == 1 or game_outcome == -2:
                                print("The computer used {}".format(cpu_action))
                                lose = rps_statement1("Sorry you lost", "-")
                                cpu_score += 1
                            else:
                                print("The computer used {}".format(cpu_action))
                                win = rps_statement1("You Win!!!","-")
                                user_score += 1

                            valid = True
                            rounds_played += 1

                            if cpu_score == win:
                                print("The computer beat you")
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

    games_played += 1
    if games_play == "c" or games_play == "continuous":
        keep_going = input("Press <enter> to play again or any key to quit ")
    elif games_play == "r" or games_play == "round":
        if games_played == games_number:
            print("Thanks for playing")
            keep_going = "stop"

print()
print("Outcome for Each Round")
list_count = 1
for item in game_summary:
    print("Round {}: {}".format(list_count, item))
    list_count += 1
