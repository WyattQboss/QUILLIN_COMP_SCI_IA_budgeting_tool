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
'''
# build GUI that populates from the CSV file. Focus on text box creation from CSV file.

from tkinter import *
master = Tk()
master.config()
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


Expense_Name_Entry = tkinter.Entry(master)
def enter_data():
    Expense_name = Expense_Name_Entry.get()

print(Expense_Name_Entry)
redbutton = Button(master, text = 'Add Expense', fg ='green', command = enter_data)
redbutton.grid( row=5, column=5)
mainloop()

import tkinter as tk

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')


# Function for getting Input
# from textbox and printing it
# at label widget

def printInput():
    inp = inputtxt_1.get(1.0, "end-1c")
    lbl.config(text="Provided Input: " + inp)

    inp = inputtxt_2.get(1.0, "end-1c")
    lbl.config(text="Provided Input: " + inp)

    inp = inputtxt_3.get(1.0, "end-1c")
    lbl.config(text="Provided Input: " + inp)

    inp = inputtxt_4.get(1.0, "end-1c")
    lbl.config(text="Provided Input: " + inp)


# TextBox Creation
inputtxt_1 = tk.Text(frame,height=1,width=20)
inputtxt_2 = tk.Text(frame,height=1,width=20)
inputtxt_3 = tk.Text(frame,height=1,width=20)
inputtxt_4 = tk.Text(frame,height=1,width=20)
inputtxt_1.pack()
inputtxt_2.pack()
inputtxt_3.pack()
inputtxt_4.pack()
# Button Creation
printButton = tk.Button(frame,
                        text="Print",
                        command=printInput)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text="")
lbl.pack()
frame.mainloop()
'''
