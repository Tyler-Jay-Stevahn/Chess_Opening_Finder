import csv
import re
import json
import time


# https://www.chessgames.com/chessecohelp.html
# https://www.365chess.com/eco.php

# Read CSV file and convert it to a dictionary
openings_dict = {}
with open('openings.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row if it exists
    for row in csv_reader:
        if len(row) < 1:
            print(f"Skipping row: {row} - Insufficient elements")
            continue

        # Extract opening code and name/move information using regular expressions
        match = re.match(r'([\w-]+)\s+(.*)', row[0])
        if not match:
            print(f"Skipping row: {row} - Invalid format")
            continue
        key = match.group(1)  # Opening code
        opening_and_moves = match.group(2)  # Opening name and moves

        # Find the start of move information
        move_info_start = opening_and_moves.find("1.")

        opening_name = opening_and_moves[:move_info_start].strip() if move_info_start != -1 else opening_and_moves.strip()
        move_info = opening_and_moves[move_info_start:].strip() if move_info_start != -1 else None

        if key not in openings_dict:
            openings_dict[key] = {}
        openings_dict[key][opening_name] = move_info  # Store move information

# Write the dictionary to a JSON file
with open('output_openings.json', 'w') as output_file:
    json.dump(openings_dict, output_file, indent=4)