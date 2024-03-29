import json

# Load data from surebetresults.json
with open('surebetresults.json') as f:
    games = json.load(f)

# Define function to calculate delta values
def calculate_deltas(A, B, C, x, y, z,M):
    deltaX = M*(B * C) / (A * B + A * C + B * C)
    deltaY = M*(A * C) / (A * B + A * C + B * C)
    deltaZ = M*(A * B) / (A * B + A * C + B * C)
    return deltaX, deltaY, deltaZ

# Define function to calculate M
def calculate_M(x, y, z):
    return 100 - x - y - z

# Iterate through each game and calculate new bet multiples
for game in games:
    A = game['Highest Home Odds']
    B = game['Highest Draw Odds']
    C = game['Highest Away Odds']
    x = game['Home Bet Multiple']
    y = game['Draw Bet Multiple']
    z = game['Away Bet Multiple']

    # Calculate M
    M = calculate_M(x, y, z)

    # Calculate deltas
    deltaX, deltaY, deltaZ = calculate_deltas(A, B, C, x, y, z,M)

    # Update bet multiples
    x += deltaX
    y += deltaY
    z += deltaZ

    # Create new table for the game
    game['Home Bet Multiple'] = x
    game['Draw Bet Multiple'] = y
    game['Away Bet Multiple'] = z
    game['M'] = M

# Save the updated data to new table
with open('Multipliers.json', 'w') as f:
    json.dump(games, f, indent=4)
