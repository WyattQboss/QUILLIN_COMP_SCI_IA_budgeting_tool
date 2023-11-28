import csv
import tkinter
# expense fields
fields_1 = ['Expense Name', 'Frequency', 'Cost', 'Category']

rows_1 = [['Electricity bill', 'Monthly', '400', 'Utility'],
        ['Car payment', 'Bi-Monthly', '250', 'Vehicle'],
        ['Phone bill', 'Monthly', '147', 'Tech'],
        ['Museum membership', 'Annually', '50', 'Recreation'],
        ['Gym membership', 'Monthly', '35', 'Recreation'],
        ['Spotify bill', 'Monthly', '10', 'Entertainment']]
#REPEATING EXPENSES CSV.FILE
filename_1 = "repeating_expenses.csv"

# writing to the expense file
with open(filename_1, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields_1)
    csvwriter.writerows(rows_1)


filename_1 = "repeating_expenses.csv"


fields_1 = []
rows_1 = []
#reading the expense file
with open(filename_1, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows_1.append(row)
    print("Total no. of rows: %d" % (csvreader.line_num))

#I took this from the geeksforgeeks code
print('Field names are:' + ', '.join(field for field in fields))


for row in rows_1:
    for col in row:
        print(col)
    print('\n')

#Dynamically create a GUI menu from a text file TKINTER

#OTHER EXPENSES CSV>FILE

fields_2 = ['Expense Name', 'Cost', 'Category']

rows_2 = [['Haircut', '20', 'Cosmetic'],
        ['Ice Cream', '5', 'Food'],
        ['Uber', '13', 'Transportation'],
        ['Movie Tickets', '18', 'Recreation'],
        ['Dinner Date', '35', 'Food'],
        ['New Keyboard', '90', 'Entertainment']]
filename_2 = "other_expenses.csv"

# writing to the expense file
with open(filename_2, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields_2)
    csvwriter.writerows(rows_2)


filename_2 = "other_expenses.csv"


fields_2 = []
rows_2 = []
#reading the expense file
with open(filename_2, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows_2.append(row)
    print("Total no. of rows: %d" % (csvreader.line_num))

#I took this from the geeksforgeeks code
print('Field names are:' + ', '.join(field for field in fields))


for row in rows_2:
    for col in row:
        print(col)
    print('\n')

# build GUI that populates from the CSV file. Focus on text box creation from CSV file.


#REPEASTING EXPENSES
from tkinter import *
master = Tk()
master.config()
master.title("Repeating Expenses")
Box_1 = Label(master, text='Expense Name').grid(row=0)
Box_2 = Label(master, text='Frequency').grid(row=1)
Box_3 = Label(master, text='Cost').grid(row=2)
Box_4 = Label(master, text='Category').grid(row=3)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)


def enter_data():
    Expense_name_1 = e1.get()
    Expense_name_2 = e2.get()
    Expense_name_3 = e3.get()
    Expense_name_4 = e4.get()
    print(Expense_name_1, Expense_name_2, Expense_name_3, Expense_name_4)
button = Button(master, text = 'Add Expense', fg ='green', command = enter_data)
button.grid( row=5, column=5)
mainloop()




#OTHER EXPENSES
master_0 = Tk()
master_0.config()
master_0.title("Other Expenses")
Box_A = Label(master_0, text='Expense Name').grid(row=0)
Box_B = Label(master_0, text='Cost').grid(row=1)
Box_C = Label(master_0, text='Category').grid(row=2)
w1 = Entry(master_0)
w2 = Entry(master_0)
w3 = Entry(master_0)

w1.grid(row=0, column=1)
w2.grid(row=1, column=1)
w3.grid(row=2, column=1)

def enter_data():
    Expense_name_A = w1.get()
    Expense_name_B = w2.get()
    Expense_name_C = w3.get()

    print(Expense_name_A, Expense_name_B, Expense_name_C)
button_0 = Button(master_0, text = 'Add Expense', fg ='green', command = enter_data)
button_0.grid( row=5, column=5)
mainloop()

