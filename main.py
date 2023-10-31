import csv

# expense fields
fields = ['Expense Name', 'Frequency', 'Cost', 'Category']

rows = [['Electricity bill', 'Monthly', '400', 'Utility'],
        ['Car payment', 'Bi-Monthly', '250', 'Vehicle'],
        ['Phone bill', 'Monthly', '147', 'Tech'],
        ['Museum membership', 'Annually', '50', 'Recreation'],
        ['Gym membership', 'Monthly', '35', 'Recreation'],
        ['Spotify bill', 'Monthly', '10', 'Entertainment']]

filename = "repeating_expenses.csv"

# writing to the expense file
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)


filename = "repeating_expenses.csv"


fields = []
rows = []
#reading the expense file
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d" % (csvreader.line_num))

#I took this from the geeksforgeeks code
print('Field names are:' + ', '.join(field for field in fields))

print('\nFirst 6 rows are:\n')
for row in rows[:6]:
    for col in row:
        print("%10s" % col, end=" "),
    print('\n')

