# Dependencies
import csv
import os
# Files to load and output (Remember to change these)
csv_path = os.path.join('Resources', 'budget_data.csv')

#variable list
#Counting the total number of months in the dataset
month_counter = 0
#Counting the number of months (i.e. "rows")
net_total = 0
#Counting the total income over all the months (i.e. the value of each month)
net_change_list = []
#this puts the net change into a list
greatest_increase = 0
#Starting point for the greatest increase in profits
greatest_decrease = 0
#Starting point for the greatest loss in profits
initial_profit_change = 0
month_profit_change = 0
#Starting point for month change
monthly_change = []
# Define this one
date_array = []


# Read the csv and convert it into a list of dictionaries
with open(csv_path) as budget_data_file:
    csv_reader = csv.reader(budget_data_file)
    # Read the header row
    header = next(csv_reader)
    print(header)

    #NOTE TO SELF, "Budget data file is the "Piece of paper"  and the reader is the "scanner"

    # Extract first row to avoid appending to net_change_list
    first_row = next(csv_reader)
    month_counter = month_counter + 1
    net_total = net_total + int(first_row[1])   
    prev_month_value = int(first_row[1])
    
    #FINDGING THE GREATEST INCREASE IN PROFITS
        # needed variables:
            # Month Counter, which is already created
            # greatest_increase, which is a modified version of net_total 
    #repeat action... first_row = next(csv_reader)
    #repeat action...month_counter = month_counter + 1
    #greatest_increase =  if X > X+1, then answer is x. Otherwise, X+1. Sooo
 
    for i in csv_reader:        
        #with python, i don't need to tell the code to stop iterating like we did with vba
        month_counter = month_counter + 1
        net_total = net_total + int(i[1])
        # so we're the net total and adding it to the next i value, but also taking the i and turning it into an intiger   

        #TRACKING NET CHANGE
        net_change = int(i[1]) - prev_month_value
        prev_month_value = int(i[1])
        net_change_list.append(net_change)

    ########Greatest increase/decrease is assessing intial month - next month, then comparing that value for every next set of months...  
    
        month_profit_change = int(i[1]) - (initial_profit_change) 
        initial_profit_change = int(i[1])
        monthly_change.append(month_profit_change)

        greatest_increase = max(monthly_change)
        greatest_decrease = min(monthly_change)


        date_array.append(i[0])
        date_increase = date_array[monthly_change.index(greatest_increase)]
        date_decrease = date_array[monthly_change.index(greatest_decrease)]






    average_net_worth = sum(net_change_list) / len(net_change_list)


    #Formatting
    net_total_formatted = '${:,.2f}'.format(net_total)
    average_net_worth_formatted = '${:,.0f}'.format(average_net_worth)
    greatest_increase_formatted = "("+ '${:,.0f}'.format(greatest_increase) + ")"
    greatest_decrease_formatted = "(" + '${:,.0f}'.format(greatest_decrease) + ")"


    #Print List:
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: ", month_counter)
    print("Total:", net_total_formatted)
    print("Average Change:", average_net_worth_formatted)
    print("Greatest Increase in profits:", date_increase, "(", greatest_increase_formatted, ")")
    print("Greatest Decrease in profits:", date_decrease, "(", greatest_decrease_formatted, ")")
    

#Printing File to Text File
csv_output_path = os.path.join('Analysis\\budget_analysis.txt')

#Printing File to Text File
with open(csv_output_path, 'w') as output_file:

    #What is going to be printed
    budget_output= (
    f"Financial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {month_counter}\n"
    f"Total: {net_total_formatted}\n"
    f"Average Change:{average_net_worth_formatted}\n"
    f"Greatest Increase in profits: {date_increase}  {greatest_increase_formatted}\n"
    f"Greatest Decrease in profits: {date_decrease} {greatest_decrease_formatted}")
   
   #Comand to print the file
    print(budget_output)
    
    #Where to print the file the file
    output_file.write(budget_output)


