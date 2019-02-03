# Import the necessary modules
import os
import csv

# Set the file path for the data set
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Set up variables to track data
num_months = 0
net_revenue = 0
avg_revenue_change = 0
greatest_inc_month = ""
greatest_inc_revenue = 0
greatest_dec_month = ""
greatest_dec_revenue = 0

