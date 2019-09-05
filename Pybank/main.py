import os
import csv

budget_data_csv = os.path.join('budget_data.csv')

with open(csvpath, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

def print_totals(budget_data):

    months = int(budget_data[0])



