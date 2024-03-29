import os
import csv

budget_data_csv = os.path.join('budget_data.csv')

#def bankingInfo(budgetData)
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

profLoss= []
date = []


avgChange = 0
months = 0
netTotal = 0
greatestDecreaseData = ''
greatestDecreaseTotal = 0
greatestIncreaseDate = ''
greatestIncreaseTotal = 0
lineBreak = "-"*30


with open('budget_data.csv') as data:
    data_reader = csv.reader(data)
    next(data_reader, None)


    for row in data_reader:

        date.append(row[0])
        profLoss.append(int(row[1]))

        value = int(row[1])

        if greatestIncreaseTotal < value:
            greatestIncreaseTotal = value
            greatestIncreaseDate = row[0]

        if greatestDecreaseTotal > value: 
            greatestDecreaseTotal = value 
            greatestDecreaseData = row[0]


        months = months + 1
        netTotal = netTotal + int(row[1])
        avgChange = mean(profLoss) 

    #formatting to two decimal places
    netTotal = "${:0,.2f}".format(netTotal)
    avgChange = "${:0,.2f}".format(avgChange)
    greatestDecreaseTotal = "${:0,.2f}".format(greatestDecreaseTotal)
    greatestIncreaseTotal = "${:0,.2f}".format(greatestIncreaseTotal).replace('$-','-$')


    txtFileInfo = f"Financial Analysis"'\n'f"{lineBreak}"'\n'f"Total Months: {months}"'\n'f"Total: ${netTotal}"'\n'f"Average Change: {avgChange}"'\n'f"Greatest increase in Profits: {greatestIncreaseDate} {greatestIncreaseTotal}"'\n'f"Greatest decrease in Profits: {greatestDecreaseData} {greatestDecreaseTotal}"

    print(txtFileInfo)

    txtFile = open("bankFile.txt","w")
    with open("bankFile.txt","w") as att_file:
        att_file.write(txtFileInfo)

