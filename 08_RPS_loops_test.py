Choice = int(input("1 or 2"))

if Choice == 1:
    rounds = int(input("Rounds:"))

roundsplayed = 0
keepgoing = ""
while keepgoing == "":
    # Main code goes here
    rps = input("rock paper or scissors")
    roundsplayed += 1
    if Choice == 2:
        keepgoing = input("Play Again?")
    if Choice == 1:
        if roundsplayed == rounds:
            keepgoing = "end"
