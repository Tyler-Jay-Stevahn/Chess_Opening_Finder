import json

print("--------------------")
print("Starting")

# Load the contents of the JSON file into the Openings dictionary
with open('output_openings.json', 'r') as json_file:
    Openings = json.load(json_file)

def find_longest_opening(pgn_moves):
    longest_match = ("", "")  # Initialize with empty values
    max_move_length = 0
    #for move_sequences in pgn_moves:
    #    print(move_sequences)
    for opening, variations in Openings.items(): # get the key/value pairs in the dictionary
        for opening_name, move_sequence in variations.items(): # get the key/value pairs in the subdictionaries
            if move_sequence in pgn_moves:
                # print(pgn_moves, "is in", opening_name)
                # print(move_sequence, len(move_sequence))
                if len(move_sequence) > max_move_length: # If it is longer the current longest match.

                    longest_match = (opening, opening_name)
                    max_move_length = len(move_sequence)
                    # print("opening name", opening_name, longest_match[1])
                    # print("Length of moves", move_sequence, len(move_sequence), "in", opening_name, longest_match[0])
                    # print("Variation", variations)
                    # print(opening_name, move_sequence,"test", len(longest_match[0]), len(longest_match[1]))
    
    return longest_match if longest_match[0] else (None, None) # return the longest value 

def parse_pgn_file(file_path):
    with open(file_path, 'r') as file:
        pgn_moves = []
        for line in file:
            if line.startswith('1.'):
                pgn_moves.extend(line.split()[0:])
        # print(pgn_moves, "pgn moves")
    return ' '.join(pgn_moves)

# Example PGN file path
pgn_file_path = 'test.pgn'

pgn_moves = parse_pgn_file(pgn_file_path)
print("--------------------")
print("Finding opening for moves:", pgn_moves)
opening, variation = find_longest_opening(pgn_moves)


print("--------------------")

if opening:
    print(f"Longest Opening: {opening}")
    if variation:
        print(f"Variation: {variation}")
else:
    print("Opening not found.")
print("--------------------")