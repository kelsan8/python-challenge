# Import the necessary modules
import os
import csv

# Set the file path for the data set
csvpath = os.path.join("C:/Users/keber/Desktop/Data Science Boot Camp/Resources/election_data.csv")

# Set up variables (and a list) to track the data
total_votes = 0 
candidate_votes = 0
candidates = []
candidate_name = ""
vote_percentage = []
winning_votes = 0
num_votes_candidate = []
election_winner = ""
candidates_list = {}

# Open the data file
with open(csvpath, newline = "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    # Skips the header row when reading data
    header = next(csv_reader, None)

    # Sets the row to read data from
    row = next(csv_reader, None)

    # Cycles through all of the rows (except the header) in the file
    for row in csv_reader:

        # Sets the initial candidate name to the first value read in column 3
        candidate_name = row[2]

        # Increments the total votes accumulator by 1 for each row
        total_votes = total_votes + 1

        # If the value in candidate_name is found in the candidates list
            # the candidate number will be set to the index number of the candidate in question
            # Then the corresponding num_votes_list index number will increment by 1
            # Same with the vote_percentage index number for the corresponding candidate index
        if candidate_name in candidates:
            candidate_num = candidates.index(candidate_name)
            num_votes_candidate[candidate_num] = num_votes_candidate[candidate_num] + 1
            vote_percentage[candidate_num] = vote_percentage[candidate_num] + 1
            # Nested if statement that will compare the number of votes per candidate with the value in winning_votes
                # If it's higher, the winning vote is set to the amount of that candidate and 
                # will set the value of election_winner to the name of that candidate
            if num_votes_candidate[candidate_num] > winning_votes:
                election_winner = candidate_name
                winning_votes = num_votes_candidate[candidate_num]
                election_winner = candidate_name
        # Otherwise, the new candidate name will be added to the candidates list along with number of votes and vote percentage
        else:
            candidates.append(row[2])
            num_votes_candidate.append(1)
            vote_percentage.append(1)

    # Counts the number of candidates based on the candidates list
    num_candidates = len(candidates)

    # Creates a new list to keep the total percentage of votes each candidate received
    candidate_total_percent = []
    # Loops through the number of candidates to calculate their percentage of votes and adds it to the 
        # candidate_total_percent list
    for i in range(num_candidates):
        candidate_percent = (vote_percentage[i] / total_votes) * 100
        candidate_total_percent.append(candidate_percent)

    
# Prints the election results to the terminal with a loop to print each candidate's results
print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
for x in range(num_candidates):
    print(f'{candidates[x]}: {candidate_total_percent[x]}% ({vote_percentage[x]})')
print("-------------------------")
print(f'Winner: {election_winner}')
print("-------------------------")

# Creates a new file to write the results to
output_path = os.path.join("C:/Users/keber/Desktop/Data Science Boot Camp/python-challenge/pypoll_output.txt")

# Opens the file in write mode to print the results, using the same loop to print each candidate's results
with open(output_path, 'w') as writefile:
    writefile.writelines("Election Results \n")
    writefile.writelines("------------------------- \n")
    writefile.writelines(f'Total Votes: {total_votes} \n')
    writefile.writelines("------------------------- \n")
    for x in range(num_candidates):
        writefile.writelines(f'{candidates[x]}: {candidate_total_percent[x]}% ({vote_percentage[x]}) \n')
    writefile.writelines("------------------------- \n")
    writefile.writelines(f'Winner: {election_winner} \n')
    writefile.writelines("------------------------- \n")

