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

    for row in csv_reader:

        # candidates.append(row[2])

        # num_votes_candidate.append(0)

        # vote_percentage.append(0)

        candidate_name = row[2]

        total_votes = total_votes + 1

        #if candidate_name == row[2]:
            # Set an accumulator for the if statement
            #x = 1
            # Add x to the candidate votes accumulator
            #candidate_votes = x

        # if row[2] = candidate_name: 
        # if candidate in candidates: ...?

        #if row[2] in candidates_list.keys():
            #candidates_list(row[2]) = candidates_list(row[2]) + 1

        #else:
            #candidates_list(row[2]) = 1

        if candidate_name in candidates:
            candidate_num = candidates.index(candidate_name)
            num_votes_candidate[candidate_num] = num_votes_candidate[candidate_num] + 1
            vote_percentage[candidate_num] = vote_percentage[candidate_num] + 1
            if num_votes_candidate[candidate_num] > winning_votes:
                election_winner = candidate_name
                winning_votes = num_votes_candidate[candidate_num]
                election_winner = candidate_name
        else:
            candidates.append(row[2])
            num_votes_candidate.append(1)
            vote_percentage.append(1)

    num_candidates = len(candidates)

    candidate_total_percent = []
    for i in range(num_candidates):
        candidate_percent = (vote_percentage[i] / total_votes) * 100
        candidate_total_percent.append(candidate_percent)

    

print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
for x in range(num_candidates):
    print(f'{candidates[x]}: {candidate_total_percent[x]}% ({vote_percentage[x]})')
print("-------------------------")
print(f'Winner: {election_winner}')
print("-------------------------")

output_path = os.path.join("C:/Users/keber/Desktop/Data Science Boot Camp/python-challenge/pypoll_output.txt")

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

