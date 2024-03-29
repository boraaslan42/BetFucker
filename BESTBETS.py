import json

# Load data from multipliers.json
with open('Multipliers.json') as f:
    games = json.load(f)

# Iterate through each game and calculate profit
for game in games:
    home_profit = game['Home Bet Multiple'] * game['Highest Home Odds']
    draw_profit = game['Draw Bet Multiple'] * game['Highest Draw Odds']
    away_profit = game['Away Bet Multiple'] * game['Highest Away Odds']
    profit = min(home_profit, draw_profit, away_profit) - 100
    game['PROFIT'] = profit

# Save the updated data to SUREBETS.json
with open('SUREBETS.json', 'w') as f:
    json.dump(games, f, indent=4)
