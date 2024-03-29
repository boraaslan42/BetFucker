import json
import os

# Load data from Multipliers.json in the Intermediatevalues folder
input_file_path = os.path.join("Intermediatevalues", "Multipliers.json")
with open(input_file_path) as f:
    games = json.load(f)

# Iterate through each game and calculate profit
for game in games:
    home_profit = game['Home Bet Multiple'] * game['Highest Home Odds']
    draw_profit = game['Draw Bet Multiple'] * game['Highest Draw Odds']
    away_profit = game['Away Bet Multiple'] * game['Highest Away Odds']
    profit = min(home_profit, draw_profit, away_profit) - 100
    game['PROFIT'] = profit

# Sort the games by profit
games_sorted = sorted(games, key=lambda x: x['PROFIT'], reverse=True)

# Save the updated data to SUREBETS.json in the base folder
output_file_path = "SUREBETS.json"
with open(output_file_path, 'w') as f:
    json.dump(games_sorted, f, indent=4)
