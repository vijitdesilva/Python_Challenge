# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 22:08:01 2021

@author: Viji
"""
# import work environment to python 
import os
# import csv library 
import csv


    #create variables for profit calculations # set up months, profit and profit change to 0 to overcome adding values errornously. 
month_count = 0
total_profit = 0
total_profit_change = 0

    # set repeat code once for each data file in csv 
for file_count in range(2):
    file_name = "budget_data" + str(file_count+1) + ".csv"

    #create path
    file_path = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

    #open file and create file handle
    with open(file_path,newline="") as csv_file:
        csv_reader = csv.reader(csv_file)

    #skip header row
        row = next(csv_reader,None)

    # read and store data from first line of csv 
        row = next(csv_reader,None)
        
    # set up vatiables to store data for calculations 
        max_month = row[0]  # maximum = Greatest profit month 
        min_month = row[0]  # minimum = Lowest profit month 
        profit = float(row[1])
        min_profit = profit
        max_profit = profit
        monthly_profit = profit
        month_count = 1
        total_profit = float(row[1])
        total_profit_change = 0

    # For loop to read one row at a time 
        for row in csv_reader:

    # Set the data counter increased by 1 for each new line reading and then store the value in second row as profit 
            month_count = month_count + 1
            profit = float(row[1])

    # adding total of profit for data set
            total_profit = total_profit + profit

    # calculation of profit change
            profit_change = profit - monthly_profit

    # calculate total profit change per month profit/loss
            total_profit_change = total_profit_change + profit_change

    # Apply if conditional to deternime  maximum profit month and the value  
            if profit_change > max_profit:
                max_month = row[0]
                max_profit = profit_change
                
    # Apply if conditional to deternime  maximum profit month and the value 
            if profit_change < min_profit:
                min_month = row[0]
                min_profit = profit_change

    # set monthly profit to profit, it will keep the profit in memory
            monthly_profit = profit

    # Calculatins of average profit and average profit change for the entire dataset 
        average_profit = total_profit/month_count
        average_profit_change = total_profit_change/(month_count-1)
        formatted_total_profit = round(total_profit)
        formatted_average_profit_change = round(average_profit_change, 2)
        formatted_max_profit = round(max_profit)
        formatted_min_profit = round(min_profit)
# print the calculations to console with proper format change 
print("\nFinancial Analysis\n---------------------")
print(f"Total Months: {month_count}")
print(f"Total: $ {formatted_total_profit}")
print(f"Average Change: $ {formatted_average_profit_change}")
print(f"Greatest Increase in Profits: {max_month} ($ {formatted_max_profit})")
print(f"Greatest Decrease in Profits: {min_month} ($ {formatted_min_profit})")

# Get the report as a text file with format change #with open('path/to/file.txt', 'r') 
#with open('path/to/file.txt', 'r') 
with open('Financial_Analysis.txt', 'w') as text:   
    text.write("  Financial Analysis"+ "\n")
    text.write("--------------------------------\n")
    text.write("  Total Months: " + str(month_count) + "\n")
    text.write("  Total Profits: " + "$" + str(formatted_total_profit) +"\n")
    text.write("  Average Change: " + '$' + str(float(formatted_average_profit_change)) + "\n")
    text.write("  Greatest Increase in Profits: " + str(max_month) + " ($" + str(formatted_max_profit) + ")\n")
    text.write("  Greatest Decrease in Profits: " + str(min_month) + " ($" + str(formatted_min_profit) + ")\n")
    text.close()
#report = open('pyBank.txt','w')

#report.close() 
