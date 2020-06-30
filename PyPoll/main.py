#! python3
## main.py - Aggregates Results based on Poll Data
import csv, sys, os

csvPath = os.path.join(".", "Resources", "election_data.csv")

votes = 0
candidates = {}
num_votes = 0
winner = ""
space = r"-----------------------" 
can_list = []

with open(csvPath, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    csv_header = next(csv_reader)
    for row in csv_reader:
        if row[0] != "":
            votes += 1
            if row[2] not in candidates.keys():
                candidates[row[2]] = {}
                candidates[row[2]]["votes"] = 1
            else:
                candidates[row[2]]["votes"] += 1
    vote_getters = [i for i in candidates.keys()]
    for k, v in candidates.items():
        for j in v:
            if int(v[j]) > num_votes:
                num_votes = int(v[j])
                winner = str(k)
            else:
                next

    print("ELECTION RESULTS")
    print(space)
    print(f"Total Votes: {votes}")
    print(space)
    for can in vote_getters:
        percent = float((candidates[can]["votes"] / votes) * 100)
        percent = round(percent, 3)
        percent = str(percent) + "%"
        print(f'{can}: {percent} ({candidates[can]["votes"]})')
        can_list.append(f'{can}: {percent} ({candidates[can]["votes"]})')
    print(space)
    print(f"Winner: {winner}")
    print(space)

    csvfile.close()
    
textPath = os.path.join(".", "Analysis", "results.txt")
with open(textPath, "w") as resultfile:
    resultfile.write("ELECTION RESULTS\n")
    resultfile.write(space + "\n")
    resultfile.write("Total Votes: " + str(votes) + "\n")
    resultfile.write(space + "\n")
    resultfile.write(can_list[0] + "\n")
    resultfile.write(can_list[1] + "\n")
    resultfile.write(can_list[2] + "\n")
    resultfile.write(can_list[3] + "\n")
    resultfile.write(space + "\n")
    resultfile.write(f"Winner: {winner}" + "\n")
    resultfile.write(space + "\n")
    resultfile.close()
            
            
                
            
    
