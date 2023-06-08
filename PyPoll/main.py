# Import Libraries:
import csv
import os

# Define the path for CSV file:
csvpath = os.path.join("Resources", "election_data.csv")

# Define variables:
total_votes = 0
candidates_votes = {}
winning_candidate = ""
winning_votes = 0

# Open CSV file:
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Skip the header:
    next(csvreader)

    #
    for row in csvreader:

        # Total number of votes cast
        total_votes += 1

        # A complete list of candidates who received votes
        candidate_name = row[2]

        if candidate_name not in candidates_votes:
            candidates_votes[candidate_name] = 0

        # The total number of votes each candidate won
        candidates_votes[candidate_name] += 1

# The winner of the election based on popular vote
for candidate, votes in candidates_votes.items():
    if votes > winning_votes:
        winning_votes = votes
        winning_candidate = candidate

# Print and export the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# The percentage of votes each candidate won
for candidate, votes in candidates_votes.items():
    vote_percentage = (votes / total_votes) * 100
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

# Export election_results.txt
with open("election_results.txt", "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")

    for candidate, votes in candidates_votes.items():
        vote_percentage = (votes / total_votes) * 100
        text_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winning_candidate}\n")
    text_file.write("-------------------------\n")
