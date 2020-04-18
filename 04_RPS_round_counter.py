# RPS Component 4 - Display round information for the user and also get the max amount of rounds

# To do
# Check that the user input is an even number so there will never be a tie
# Ensure that the number of rounds is printed

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

while round_continue == "yes":
    rounds = intcheck("The game will be best out of what (Must be an odd number)? ")

    if (rounds % 2) == 1:
        rounds_played = 0

        while rounds_played < rounds:
            print("Round {}".format(rounds_played + 1))
            rounds_played += 1

        print("You have gotten to the end of the game")
        round_continue = "no"

    else:
        print("Please enter an odd number as to ensure no ties")
        print()
