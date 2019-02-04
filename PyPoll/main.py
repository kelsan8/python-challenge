# Import the necessary modules
import os
import csv

# Set the file path for the data set
csvpath = os.path.join("C:/Users/keber/Desktop/Data Science Boot Camp/Resources/election_data.csv")

# Set up variables (and a list) to track the data
num_votes = 0 
candidates = []
vote_percentage = 0
num_votes_candidate = 0
election_winner = ""