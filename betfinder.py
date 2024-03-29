import json

# Load data from games.json
with open('games.json') as f:
    games = json.load(f)

# Define function to calculate smallest multiples exceeding balance
def calculate_multiples(balance, odds):
    multiples = {}
    for key, value in odds.items():
        if value > 0:
            multiples[key] = balance / value
    return multiples

# Iterate through each game and calculate multiples
for game in games:
    home_multiples = calculate_multiples(100, {'Highest Home Odds': game['Highest Home Odds']})
    draw_multiples = calculate_multiples(100, {'Highest Draw Odds': game['Highest Draw Odds']})
    away_multiples = calculate_multiples(100, {'Highest Away Odds': game['Highest Away Odds']})

    # Add multiples to the game
    game['Home Bet Multiple'] = home_multiples.get('Highest Home Odds', None)
    game['Draw Bet Multiple'] = draw_multiples.get('Highest Draw Odds', None)
    game['Away Bet Multiple'] = away_multiples.get('Highest Away Odds', None)

# Save the updated data to surebetresults.json
with open('surebetresults.json', 'w') as f:
    json.dump(games, f, indent=4)
