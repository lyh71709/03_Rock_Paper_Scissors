game_mode = int(input("1 or 2"))

if Choice == 1:
    rounds = int(input("Rounds:"))

roundsplayed = 0
keepgoing = ""
while keepgoing == "":
  
    # Main code goes here
    rps = input("rock paper or scissors")
    roundsplayed += 1
    if game_mode == 2:
        keepgoing = input("Play Again?")
    if game_mode == 1:
        if roundsplayed == rounds:
            keepgoing = "end"
