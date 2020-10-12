#Import the modules I need
import os
import csv

#connect to the csv path and make it so I can write my code
csvpath = os.path.join ("Resources", "budget_data.csv")

#create a path to a txt file with my analysis
outpath = os.path.join ("Analysis", "budget_data.txt")

#open my csv as a filepath from a comma delimited file
with open (csvpath) as filepath:
    csvreader = csv.reader(filepath, delimiter=',')

    print(csvreader)
    #bring in the headers from the csv
    csv_header = next(csvreader)
    #print the headers
    print(f"CSV Header: {csv_header}")

    #define my variables
    total=0
    totalprofitlosses=0
    totalchange=0
    previous=0
    greatestincrease=0
    greatestmonth = ""
    greatestdecrease=99999999999
    decreasemonth = ""
    averagechange=0

    #for the rows in the reader, get my totals
    for row in csvreader:
        total=total+1
        totalprofitlosses=totalprofitlosses + int(row[1])

        if total > 1:

            #get my total change and average change
            change=int(row[1])-previous
            totalchange=totalchange + change
            averagechange=round(totalchange/(total-1), 2)
            #get the greatest increase in profits
            if change > greatestincrease:
                greatestincrease=change
                greatestmonth = row[0]
            
            #get the greatest decrease in profits
            if change < greatestdecrease:
                greatestdecrease = change
                decreasemonth = row[0]

        previous=int(row[1])
        

#print my results       
print("Financial Analysis")
print("--------------------")
print("Total Months:  "+str(total))
print("Total:  $"+str(totalprofitlosses))
print("Average Change: $" +str(averagechange))
print("Greatest Increase in Profits:  " + greatestmonth +" $"+str(greatestincrease))
print("Greatest Decrease in Profits:  " + decreasemonth +" $"+str(greatestdecrease))

#send the results to a txt file
with open (outpath, "w") as textfile:
    textfile.write ("Financial Analysis\n")
    textfile.write ("--------------------\n")
    textfile.write("Total Months:  "+str(total)+"\n")
    textfile.write("Total:  $"+str(totalprofitlosses)+"\n")
    textfile.write("Average Change: $" +str(averagechange)+"\n")
    textfile.write("Greatest Increase in Profits:  " + greatestmonth +" $"+str(greatestincrease)+"\n")
    textfile.write("Greatest Decrease in Profits:  " + decreasemonth +" $"+str(greatestdecrease)+"\n")
    