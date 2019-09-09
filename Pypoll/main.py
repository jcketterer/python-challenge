import os
import csv

#Setting Dictionary for candidates
candidatedict = {}

#Setting total votes variable
total_votes = 0
line_break = "-"*30

#Setting path for CSV file 
path = os.path.join("election_data.csv")

with open (path,newline="") as data:
    data_reader = csv.reader(data,delimiter=',')
    data_header = next(data_reader)

    for row in data_reader:
        total_votes += 1
        if row[2] not in candidatedict:
            candidatedict[row[2]] = 0
        candidatedict[row[2]] += 1

txtFileInfo = f"Election Results"'\n'f"{line_break}"'\n'f"Total Votes: {total_votes}"
print(txtFileInfo)

with open ("Election Results.txt", 'w') as f:
    f.write(f"Election Results\n")
    f.write(f"{line_break}\n")
    f.write(f"Total Votes: {total_votes}\n")


    for key,value in candidatedict.items():
        print(key,"  ", str(round((value/total_votes)*100,2)),"% ", value)
        f.write(f"{key} {round((value/total_votes)*100,2)}% {value}\n")
    print(line_break)
    print("Winner:", str(max(candidatedict, key=candidatedict.get)))
    f.write(f"{line_break}\n")
    f.write(f"Winner :{max(candidatedict, key=candidatedict.get)}\n")
