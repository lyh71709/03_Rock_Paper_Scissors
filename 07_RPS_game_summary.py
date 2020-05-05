# RPS Component 7 - Get  game summary to show the user

game_summary = ["User Win", "CPU Win", "User Win", "CPU Win", "User Win"]

# print game outcomes
print("Outcome for Each Round")
list_count = 1
for item in game_summary:
    print("Round {}: {}".format(list_count, item))
    list_count += 1
