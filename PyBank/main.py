# Import the necessary modules
import os
import csv

# Set the file path for the data set
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Set up variables to track data
num_months = 1
net_revenue = 0
revenue_change = 0
avg_revenue_change = 0
row_revenue = 0
last_revenue = 0


# Open the data file
with open(csvpath, newline = "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    row_revenue = float(row[1])
    greatest_inc_month = row[0]
    greatest_inc_revenue = row_revenue
    greatest_dec_month = row[0]
    greatest_dec_revenue = row_revenue

    # Skips the header row
    header = next(csv_reader, None)

    # Cycle through each row in the data file to grab data
    for row in csv_reader:

        # Grabs the revenue value for the row of the iteration
        # row_revenue = long(row[1])

        # Increments the net_revenue by the revenue of the current row
        net_revenue = net_revenue + row_revenue

        # Calculates the change in the revenue from the current row from the previous row
        revenue_change = row_revenue - last_revenue

        # Increments the change in revenue to average later
        avg_revenue_change = avg_revenue_change + revenue_change

        # Increments the number of months by 1 for each iteration
        num_months = num_months + 1

        if row_revenue > greatest_inc_revenue:
            greatest_inc_month = row[0]
            greatest_inc_revenue = revenue_change

        if row_revenue < greatest_dec_revenue:
            greatest_dec_month = row[0]
            greatest_dec_revenue = revenue_change

        # Resets the value of the previous row's revenue value to use in the next calculation
        last_revenue = float(row[1])

