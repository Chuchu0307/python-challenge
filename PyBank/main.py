import os
import csv
budget_data_csv = os.path.join("Resources","budget_data.csv")

total_month = 0 
total_net = 0
net_change_list =[]

greatest_increase = 0
greatest_increase_date = "" 
greatest_decrease= 0
greatest_decrease_date = "" 


with open(budget_data_csv) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        total_month += 1
        profit_loss = int(row[1])
        total_net += profit_loss

        if total_month > 1:
             net_change = profit_loss - previous_profit_loss
             net_change_list.append(net_change)

             if net_change > greatest_increase:
                  greatest_increase = net_change
                  greatest_increase_date = row[0]
             if net_change < greatest_decrease:
                  greatest_decrease = net_change
                  greatest_decrease_date = row[0]

        previous_profit_loss = profit_loss

    average_change = sum(net_change_list)/len(net_change_list)
  
    print("Financial Analysys")
    print("----------------------------------")
    print("Total Month: " + str(total_month))

    print("Total: " + "$"+str(total_net))

    print("Average Change: " + "$"+ str(round(average_change,2)))

    print("Greatest Increase in Profits: " + greatest_increase_date + " ($"+ str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + greatest_decrease_date + " ($"+ str(greatest_decrease) + ")")   

output_path = os.path.join("analysis", "budgest_result.txt")
with open(output_path, "w", newline= "") as datafile:
     writer = csv.writer(datafile)
     writer.writerow(["Total Month: " + str(total_month)])
     writer.writerow(["Total : " + "$" + str(total_net)])
     writer.writerow(["Average Change : " + "$" + str(average_change)])
     writer.writerow(["Greatest Increase : " + "$" + str(greatest_increase)])
     writer.writerow(["Greatest Decrease : " + "$" + str(greatest_decrease)])


     
        


     

