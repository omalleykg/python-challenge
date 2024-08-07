import os
import csv

# csv filepath
csvpath = os.path.join("..", 'Resources', 'election_data.csv')

total_votes = 0
candidate_votes = {} #dictionary to store candidate names and their total votes

with open(csvpath, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if it exists

    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2] #assuming candidate name is in the third column
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1
    
    
    #candidate_votes.append(int(row[1]))

    #first_row = next(csv_reader)
    #total_votes += 1
    #candidate_name = first_row[2]  # Assuming candidate name is in the third column of the CSV
    





print("Election Results:")
print("---------------------------------------------------------")
print("Total Votes:", total_votes )
print("---------------------------------------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {(votes/total_votes)*100:.3f}% ({votes})")
print("---------------------------------------------------------")
winner = max(candidate_votes, key=candidate_votes.get)
print("Winner:", winner)
print("---------------------------------------------------------")
print("Candidate Votes Dictionary:", candidate_votes)

# Convert an integer to a string
total_votes = 369711
total_votes_str = str(total_votes)


# Open a file in write mode ('w')
with open("output_PyPoll.txt", "w") as file:
    file.write("Election Results: " + "\n")
    file.write("---------------------------------------------------------" + "\n")
    file.write("Total Votes: " + total_votes_str + "\n")
    file.write("---------------------------------------------------------" + "\n")
    # Iterate over the candidate_votes dictionary
    for candidate, votes in candidate_votes.items():
        # Calculate the percentage of votes for each candidate
        percentage = (votes / total_votes) * 100
        # Write the candidate's name, percentage of votes, and total votes to the text file
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    
    file.write("---------------------------------------------------------" + "\n")
    file.write("Winner: " + winner + "\n")
    file.write("---------------------------------------------------------" + "\n")
