import os
import csv
election_data_csv = os.path.join("Resources","election_data.csv")

total_votes = 0
candidate_list = []
percentage = ""
candidate_name = ""
previous_candidate = ""
all_candidate = {}
winning_votes = 0
winning_percentage = 0
winner = ""


with open(election_data_csv) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader: 
        total_votes += 1
        candidate_name = row[2]

    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(total_votes)) 
    print("----------------------------")   

    if candidate_name not in candidate_list:
        candidate_list.append(candidate_name)   
        all_candidate[candidate_name] = 0
    all_candidate[candidate_name] += 1


output_path = os.path.join("analysis", "election_result.txt")
with open(output_path, "w", newline= "") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Total Votes: " + str(total_votes)])  

    for candidate_name in all_candidate:
        votes = all_candidate[candidate_name]
        percentage = round(float(votes)/float(total_votes),5)*100
        print(all_candidate)
        print(f"{candidate_name}: {percentage}% ({votes})")
        writer.writerow([candidate_name] + [percentage] + [votes])

        if (votes > winning_votes) and (percentage > winning_percentage):
            winner = candidate_name
            print(f"{winner}")
            writer.writerow(["Winner: " + f"{winner}"])
           
                            
                         


    
    






    
         
         
 
    


        
       
    

    
          





       


