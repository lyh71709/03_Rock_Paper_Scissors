# RPS Component 6 - Create statements to make the game look nicer

chosen_action = input("What is the player's action? ").lower()
cpu_action = input("What is the CPU's action? ").lower()

if chosen_action == "rock":
    user_icon = "🥔"
elif chosen_action == "paper":
    user_icon = "🧻"
elif chosen_action == "scissors":
    user_icon = "✂"

if cpu_action == "rock":
    cpu_icon = "🥔"
elif cpu_action == "paper":
    cpu_icon = "🧻"
elif cpu_action == "scissors":
    cpu_icon = "✂"

def rps_statement(statement, char):
    print()
    print(char*(len(statement)+12))
    print("{} \ {}  | {}".format(user_icon, cpu_icon, statement))
    print(char*(len(statement)+12))
    print()

print()
win = rps_statement("You Win!!!","-")

print()
lose = rps_statement("Sorry you lost", "-")

print()
draw = rps_statement("It was a draw", "-")
