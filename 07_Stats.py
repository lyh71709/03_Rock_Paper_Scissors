# RPS Component 7 - Get  game summary to show the user

game_stats = [0, 1, 0, 1, 0]



# print game outcomes
print("Outcome for Each Round")
list_count = 1
for item in game_stats:
    if item == 0:
        message = "User Win"
    elif item == 1:
        message = "CPU Win"
    print("Round {}: {}".format(list_count, message))
    list_count += 1


