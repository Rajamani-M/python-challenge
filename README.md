 # Python Challenge

This repository contains solutions for two Python challenges: PyBank and PyPoll. Each challenge involves analyzing a dataset using Python scripting. The project is organized into two main folders, each one of the challenges:
 * PyBank: Analyzing financial records.
 * PyPoll: Analyzing election poll data.
 Each folder contains:
 * main.py: The main Python script for analysis.
 * Resources/: Folder containing the CSV file used for analysis (budget_data.csv for PyBank, election_data.csv for PyPoll).
 * analysis/: Folder containing the output text file (financial_analysis.txt for PyBank, election_results.txt for PyPoll).

## Instructions

 * To run the scripts:
 * Clone this repository to your local machine usingg it clone.
 * Navigate to the challenge folder(PyBank or PyPoll).
 * Run python main.py in your terminal to execute the script.
 * View the results printed in the terminal and find detailed analysis in the text file in the analysis/ folder. 

 # PyBank Analysis
   The PyBank script calculates:
   * Total number of months included in the dataset.
   * Net total amount of "Profit/Losses" over the entire period.
   * Average change in "Profit/Losses" over the entire period.
   * Greatest increase in profits (date and amount).
   * Greatest decrease in profits (date and amount).

# PyPoll Analysis
   The PyPoll script calculates:
   * Total number of votes cast.
   * List of candidates who received votes.
   * Percentage of votes each candidate won.
   * Total number of votes each candidate won.
   * Winner of the election based on popular vote.

## Hints and Bonus

For additional help or consider these suggestions:

# Hints:
 Review Python documentation on CSV handling (`csv` module), list operations, and basic arithmetic.

## Bonus: 
Implement error handling for missing or invalid data in the CSV files.