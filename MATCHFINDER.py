import os
import json
from fuzzywuzzy import fuzz

# Function to find matches between teams in two sets of data
def find_matches(data1, data2):
    matches = []

    # Iterate through each match in the first set of data
    for match1 in data1:
        home1 = match1["Home Team"]
        away1 = match1["Away Team"]

        # Iterate through each match in the second set of data
        for match2 in data2:
            home2 = match2["Home Team"]
            away2 = match2["Away Team"]

            # Use fuzzy matching to compare team names
            if (fuzz.ratio(home1, home2) > 85 or fuzz.partial_ratio(home1, home2) > 85) and \
               (fuzz.ratio(away1, away2) > 85 or fuzz.partial_ratio(away1, away2) > 85):
                matches.append((match1, match2))

    return matches

# Function to load JSON data from a file
def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Get all .json files in the directory
json_files = [file for file in os.listdir() if file.endswith(".json") and file != "games.json" and file != "surebetresults.json" and file != "Multipliers.json" and file != "SUREBETS.json"]

# Prepare output data
output_data = []

# Load data from each file and find matches
for i in range(len(json_files)):
    for j in range(i + 1, len(json_files)):
        data1 = load_json(json_files[i])
        data2 = load_json(json_files[j])
        matches = find_matches(data1, data2)
        for match1, match2 in matches:
            home_team = match1["Home Team"]
            away_team = match1["Away Team"]
            home_odds1, draw_odds1, away_odds1 = float(match1["Home"]), float(match1["Draw"]), float(match1["Away"])
            home_odds2, draw_odds2, away_odds2 = float(match2["Home"]), float(match2["Draw"]), float(match2["Away"])
            
            # Determine the highest odds for each outcome
            highest_home_odds = max(home_odds1, home_odds2)
            highest_draw_odds = max(draw_odds1, draw_odds2)
            highest_away_odds = max(away_odds1, away_odds2)
            
            # Determine the source of the highest odds for each outcome
            if highest_home_odds == home_odds1:
                source_home = json_files[i].replace("_", " ").split(".")[0]
            else:
                source_home = json_files[j].replace("_", " ").split(".")[0]
                
            if highest_draw_odds == draw_odds1:
                source_draw = json_files[i].replace("_", " ").split(".")[0]
            else:
                source_draw = json_files[j].replace("_", " ").split(".")[0]
                
            if highest_away_odds == away_odds1:
                source_away = json_files[i].replace("_", " ").split(".")[0]
            else:
                source_away = json_files[j].replace("_", " ").split(".")[0]
            
            output_data.append({
                "Home Team": home_team,
                "Away Team": away_team,
                "Highest Home Odds": highest_home_odds,
                "Highest Draw Odds": highest_draw_odds,
                "Highest Away Odds": highest_away_odds,
                "Source Home": source_home,
                "Source Draw": source_draw,
                "Source Away": source_away
            })

# Save output data as JSON
with open("games.json", "w") as outfile:
    json.dump(output_data, outfile, indent=4)

print("Output saved as 'games.json'")
