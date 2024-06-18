import csv

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read the election data
with open('PyPoll/Resources/election_data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    for row in reader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate the percentage of votes each candidate won
percent_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# Determine the winner
for candidate, votes in candidates.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percent_votes[candidate]:.3f}% ({candidates[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
