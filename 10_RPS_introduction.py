# RPS Component 10 - Create  instructions and rules to explain to the user how the game works

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
  
# Ask user is the user wants the rules for RPSLS
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

