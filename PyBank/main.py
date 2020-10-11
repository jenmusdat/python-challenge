import os
import csv

csvpath = os.path.join ("Resources", "budget_data.csv")


outpath = os.path.join ("Analysis", "budget_data.txt")


with open (csvpath) as filepath:
    csvreader = csv.reader(filepath, delimiter=',')

    print(csvreader)
    #
    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")

    total=0
    totalprofitlosses=0
    totalchange=0
    previous=0
    greatestincrease=0
    greatestmonth = ""
    greatestdecrease=99999999999
    decreasemonth = ""
    averagechange=0

    for row in csvreader:
        total=total+1
        totalprofitlosses=totalprofitlosses + int(row[1])

        if total > 1:

            change=int(row[1])-previous
            totalchange=totalchange + change
            averagechange=round(totalchange/(total-1), 2)
            if change > greatestincrease:
                greatestincrease=change
                greatestmonth = row[0]
            
            if change < greatestdecrease:
                greatestdecrease = change
                decreasemonth = row[0]

        previous=int(row[1])
        
        
       # print(row[1])

print("Financial Analysis")
print("--------------------")
print("Total Months:  "+str(total))
print("Total:  $"+str(totalprofitlosses))
print("Average Change: $" +str(averagechange))
print("Greatest Increase:  " + greatestmonth +" $"+str(greatestincrease))
print("Greatest Decrease:  " + decreasemonth +" $"+str(greatestdecrease))

with open (outpath, "w") as textfile:
    textfile.write ("Financial Analysis\n")
    textfile.write ("--------------------\n")
    textfile.write("Total Months:  "+str(total)+"\n")
    textfile.write("Total:  $"+str(totalprofitlosses)+"\n")
    textfile.write("Average Change: $" +str(averagechange)+"\n")
    textfile.write("Greatest Increase:  " + greatestmonth +" $"+str(greatestincrease)+"\n")
    textfile.write("Greatest Decrease:  " + decreasemonth +" $"+str(greatestdecrease)+"\n")
    