import csv
import os

# Path to the CSV file
file_path = 'PyBank/Resources/budget_data.csv'

# Ensure the file exists
if not os.path.isfile(file_path):
    print(f"Error: The file '{file_path}' does not exist.")
else:
    # Initialize variables
    total_months = 0
    net_total = 0
    previous_profit_loss = None
    changes = []
    dates = []

    # Read the CSV file
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        
        for row in reader:
            date, profit_loss = row
            profit_loss = int(profit_loss)
            
            # Count the total number of months
            total_months += 1
            
            # Sum the total profits/losses
            net_total += profit_loss
            
            # Calculate the monthly change in profit/loss
            if previous_profit_loss is not None:
                change = profit_loss - previous_profit_loss
                changes.append(change)
                dates.append(date)
            
            previous_profit_loss = profit_loss

    # Calculate the average change
    average_change = sum(changes) / len(changes) if changes else 0

    # Find the greatest increase and decrease in profits
    if changes:
        greatest_increase = max(changes)
        greatest_decrease = min(changes)
        greatest_increase_date = dates[changes.index(greatest_increase)]
        greatest_decrease_date = dates[changes.index(greatest_decrease)]
    else:
        greatest_increase = 0
        greatest_decrease = 0
        greatest_increase_date = ''
        greatest_decrease_date = ''

    # Print the analysis
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
