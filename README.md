### PyBank and PyPoll
This repository contains two separate Python scripts:

1- PyBank is a financial analysis tool.
2- PyPoll is a vote-counting program for an election.

### PyBank
PyBank is a Python script that analyzes the financial records of a company, and calculates each of the following:

The total number of months included in the dataset.
The net total amount of Profit/Losses over the entire period.
The average of the changes in Profit/Losses over the entire period.
The greatest increase in profits (date and amount) over the entire period.
The greatest decrease in losses (date and amount) over the entire period.
The script takes as input a CSV file called budget_data.csv, which is located in the "Resources" directory. The CSV file should contain two columns: "Date" and "Profit/Losses".

The script outputs the analysis to both the terminal and a text file, analysis.txt, which is located in the root directory.

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

### PyPoll
PyPoll is a Python script that analyzes voting data for an election, and calculates each of the following:

The total number of votes cast.
A complete list of candidates who received votes.
The total number of votes each candidate received.
The percentage of votes each candidate won.
The winner of the election based on popular vote.
The script takes as input a CSV file called election_data.csv, which is located in the "Resources" directory. The CSV file should contain three columns: "Ballot ID", "County", and "Candidate".

The script outputs the analysis to both the terminal and a text file, election_results.txt, which is located in the root directory.

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
