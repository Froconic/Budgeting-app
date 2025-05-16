# GUI development modules
import tkinter as tk
from tkinter import messagebox  # For dialog popups
import customtkinter as ctk     # Modern-looking alternative to tkinter

# Data handling modules
import json                    # For reading/writing JSON files
import os                      # For checking file existence

# File paths for saving data
setData = "C:/Users/akira/Desktop/Stuff/Code/GitHub/Budgeting-app/setData.json"
recordFile = "C:/Users/akira/Documents/Second-Brain/Daily-Journal/2025/Monthly/Expenses.md"

# Expense class represents an expense entry in the GUI
class Expense:
    def __init__(self, name, value, row, frame):
        self.name = name
        self.value = value

        # GUI labels for expense name and value
        self.label = ctk.CTkLabel(frame, text=name)
        self.label.grid(row=row, column=1)

        self.valueLabel = ctk.CTkLabel(frame, text=value)
        self.valueLabel.grid(row=row, column=2)

# Loads JSON data from a file or returns a default structure
def loadJSON(file):
    if os.path.exists(file):
        with open(file, "r") as file:
            return json.load(file)
    return {"income": 0, "expenses": {}}  # Default fallback

# Initialize expense lists
expenseList = []
setExpenseList = []
variableExpenseList = []

# GUI initialization
ctk.set_appearance_mode("dark")
window = ctk.CTk()
window.title("Budget Calculator")
window.geometry("1500 x 1500")

# Configure window grid
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

# Frames for layout
center = ctk.CTkFrame(window)
center.grid(row=0, pady=20, padx=20)
buttonFrame = ctk.CTkFrame(window)
buttonFrame.grid(row=1, pady=10)

# Load existing data from file
budget = loadJSON(setData)

# Populate set expenses into GUI and list
setExpenses = budget["Set Expenses"]
for i, (name, value) in enumerate(setExpenses.items()):
    expense = Expense(name, value, row=4+len(expenseList), frame=center)
    expenseList.append(expense)
    setExpenseList.append(expense)

# Populate variable expenses into GUI with actual value entry fields
variableExpenses = budget["Variable Expenses"]
for i, (name, value) in enumerate(variableExpenses.items()):
    expense = Expense(name, value, row=4+len(expenseList), frame=center)
    expense.actualValue = ctk.CTkEntry(center, placeholder_text=f"Actual {expense.name}")
    expense.actualValue.grid(row=4+len(expenseList), column=3)
    expenseList.append(expense)
    variableExpenseList.append(expense)

# Load income value
income = budget["income"]

# GUI static elements
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(0, weight=1)

# Header label
program = ctk.CTkLabel(center, text="Budget Program")
program.grid(row=0, column=2, pady=10)

# Entry for month
month = ctk.CTkEntry(center, placeholder_text="Month goes here")
month.grid(row=1, column=2)

# Income display
title = ctk.CTkLabel(center, text="Income:")
title.grid(row=2, column=0)

incomeLabel = ctk.CTkLabel(center, text=income)
incomeLabel.grid(row=2, column=1)

# Labels for expenses section
expensesTitle = ctk.CTkLabel(center, text="Expenses")
expensesTitle.grid(row=3, column=0, padx=10)

actual = ctk.CTkLabel(center, text="Actual Spending")
actual.grid(row=3, column=3)

# Determine if new expense is set or variable
def setOrNah(expense):
    check = input(f"Is {expense.name} a set expense? Y/N: ")
    if check.lower() == 'n':
        # Variable expense: Add entry field
        expense.actualValue = ctk.CTkEntry(center, placeholder_text=f"Actual {expense.name}")
        expense.actualValue.grid(row=4+len(expenseList), column=3)
        expenseList.append(expense)
        variableExpenseList.append(expense)
    else:
        # Set expense
        expenseList.append(expense)
        setExpenseList.append(expense)

    # Save updated lists
    saveSetData(setExpenseList, variableExpenseList)

# Add new expense to the app
def addExpense():
    row = 4 + len(expenseList)
    name = input("Name of expense: ")
    value = int(input("Amount: "))
    expense = Expense(name, value, row, center)
    setOrNah(expense)

    # Display new expense in GUI
    expenseName = ctk.CTkLabel(center, text=name)
    expenseName.grid(row=row, column=1)

    expenseValue = ctk.CTkLabel(center, text=value)
    expenseValue.grid(row=row, column=2)

# Save all expenses into setData JSON
def saveSetData(setExpenseList, variableExpenseList):
    setExpenses = {e.name: e.value for e in setExpenseList}
    variableExpenses = {e.name: e.value for e in variableExpenseList}

    data = {
        "income": income,
        "Set Expenses": setExpenses,
        "Variable Expenses": variableExpenses
    }

    with open(setData, "w") as f:
        json.dump(data, f, indent=4)

# Calculate expected and actual savings
def savings(currentValues):
    total = 0
    variableTotal = 0
    setTotal = 0

    # Sum expected values from all expenses
    for item in expenseList:
        total += item.value

    monthly = income * 4
    expectedSavings = monthly - total

    # Sum actual values from variable expenses
    for item in currentValues:
        variableTotal += int(item)

    for item in setExpenseList:
        setTotal += item.value

    actualTotal = setTotal + variableTotal
    actualSavings = monthly - actualTotal

    return expectedSavings, actualSavings

# Save data as markdown into a journal file
def recordData(file, month, setExpenseList, variableExpenseList, currentValues, savingsData):
    with open(file, "a") as f:
        f.write(f"# {month}\n\n---\n\n")
        f.write("###  Expenses\n\n")
        f.write("| Item | Expected | Actual |\n")
        f.write("| ---- | ---- | ---- |\n")

        for item in setExpenseList:
            f.write(f"| {item.name} | {item.value} | --- |\n")

        for item in variableExpenseList:
            f.write(f"| {item.name} | {item.value} | {item.actualValue.get()} |\n")

        f.write("### Savings this month\n")
        f.write("| Expected | Actual |\n")
        f.write("| --- | --- |\n")
        f.write(f"| {savingsData[0]} | {savingsData[1]} |\n\n")
        f.write("---\n")

        messagebox.showinfo("Success", f"Data saved.\nExpected: {savingsData[0]}\nActual: {savingsData[1]}")

# Collect user inputs, calculate savings, and store the data
def submitData():
    currentMonth = month.get()
    currentValues = [item.actualValue.get() for item in variableExpenseList]
    savingsData = savings(currentValues)

    messagebox.showinfo("Saved", f"Data for {currentMonth} input")
    recordData(recordFile, currentMonth, setExpenseList, variableExpenseList, currentValues, savingsData)

# Buttons for interaction
add = ctk.CTkButton(buttonFrame, text="Add", command=addExpense)
add.grid(row=0, column=2, pady=5)

submit = ctk.CTkButton(buttonFrame, text="Submit", command=submitData)
submit.grid(row=1, column=2)

# Start GUI loop
window.mainloop()
