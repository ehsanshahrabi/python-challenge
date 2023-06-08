# Import libraries
import csv
import os

# Define the path for CSV file:
csvpath = os.path.join("Resources", "budget_data.csv")

# Define variables
total_months = 0
total_profit_losses = 0
previous_profit_losses = None
changes = []
greatest_increase = {"Date": "", "Profit/Losses": float('-inf')}
greatest_decrease = {"Date": "", "Profit/Losses": float('inf')}

# Open and read the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Skip the header row
    next(csvreader)

    for row in csvreader:
        date = row[0]
        profit_losses = int(row[1])

        # Total months
        total_months += 1

        # Total amount of Profit/Losses
        total_profit_losses += profit_losses

        # Changes in Profit/Losses
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)

            # Greatest increase in profits
            if change > greatest_increase["Profit/Losses"]:
                greatest_increase = {"Date": date, "Profit/Losses": change}

            # Greatest decrease in profits
            if change < greatest_decrease["Profit/Losses"]:
                greatest_decrease = {"Date": date, "Profit/Losses": change}

        previous_profit_losses = profit_losses

# Average change in Profit/Losses
average_change = sum(changes) / len(changes) if changes else 0

# Print the analysis
print("Financial Analysis")
print("-" * 30)
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(
    f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Profit/Losses']})")
print(
    f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Profit/Losses']})")

# Export analysis.txt
with open("analysis.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("-" * 30 + "\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(
        f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Profit/Losses']})\n")
    file.write(
        f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Profit/Losses']})\n")
