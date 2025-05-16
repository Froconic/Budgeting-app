# Import the standard tkinter module for GUI development
import tkinter as tk

# Import the messagebox module from tkinter to show pop-up messages
from tkinter import messagebox

# Import customtkinter (a styled version of tkinter with modern widgets)
import customtkinter as ctk

# Import the json module to read/write JSON files
import json

# Import the os module to interact with the file system (check if file exists)
import os

# Path to the JSON file that stores budget data
setData = "C:/Users/akira/Desktop/Stuff/Code/GitHub/Budgeting-app/setData.json"
outputFile = "C:/Users/akira/Desktop/Stuff/Code/GitHub/Budgeting-app/budget.json"
recordFile = "C:/Users/akira/Documents/Second-Brain/Daily-Journal/2025/Monthly/Expenses.md"

class Expense:
  def __init__(self, name, value, row, frame):
    self.name = name
    self.value = value
    # self.setExpense = setExpense
    
    self.label = ctk.CTkLabel(frame, text=name)
    self.label.grid(row=row, column=1)
    self.valueLabel = ctk.CTkLabel(frame, text=value)
    self.valueLabel.grid(row=row, column=2)
    
    # if setExpense == True:
    #   self.actualLabel = ctk.CTkEntry(frame, placeholder_text="name")
    #   self.actualLabel.grid(row=row, column=4)

# Function to load income and expenses data from the JSON file
def loadJSON(file):
    if os.path.exists(file):  # Check if the file exists
        with open(file, "r") as file:
            return json.load(file)  # Load and return the JSON data as a Python dictionary
    return {"income": 0, "expenses": {}}  # Return default structure if file doesn't exist

# def loadData():
  
# Extract the income and expenses from the loaded data
expenseList = []
setExpenseList = []
variableExpenseList = []
startRow = 4
  
ctk.set_appearance_mode("dark")
window = ctk.CTk()
window.title("Budget Calculator")
window.geometry("1500 x 1500")

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

center = ctk.CTkFrame(window)
center.grid(row=0, pady=20, padx=20)
buttonFrame = ctk.CTkFrame(window)
buttonFrame.grid(row=1, pady=10)

budget = loadJSON(setData)
setExpenses = []
setExpenses = budget["Set Expenses"]
for i, (name,value) in enumerate(setExpenses.items()):
  expense = Expense(name, value, row=4+len(expenseList), frame=center)
  expenseList.append(expense)
  setExpenseList.append(expense)
variableExpenses = []
variableExpenses = budget["Variable Expenses"]
for i, (name,value) in enumerate(variableExpenses.items()):
  expense = Expense(name, value, row=4+len(expenseList), frame=center)
  expense.actualValue = ctk.CTkEntry(center, placeholder_text=f"Actual {expense.name}")
  expense.actualValue.grid(row=4+len(expenseList), column=3)
  expenseList.append(expense)
  variableExpenseList.append(expense)

income = budget["income"]



# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(0, weight=1)
program = ctk.CTkLabel(center,text="Budget Program")
program.grid(row=0, column=2, pady=10)

month = ctk.CTkEntry(center, placeholder_text="Month goes here")
month.grid(row=1, column=2)

title = ctk.CTkLabel(center,text="Income:")
title.grid(row=2, column=0)

# Income
incomeLabel = ctk.CTkLabel(center,text=income)
incomeLabel.grid(row=2, column=1)

# Expenses
expensesTitle = ctk.CTkLabel(center, text="Expenses")
expensesTitle.grid(row=3, column=0, padx=10)

actual = ctk.CTkLabel(center, text="Actual Spending")
actual.grid(row=3, column=3)

def setOrNah(expense):
  check = input(f"Is {expense.name} a set expense? Y/N: ")
  if check == 'n' or check == 'N':
    expense.actualValue = ctk.CTkEntry(center, placeholder_text=f"Actual {expense.name}")
    expense.actualValue.grid(row=4+len(expenseList), column=3)
    expenseList.append(expense)
    variableExpenseList.append(expense)
    saveSetData(setExpenseList, variableExpenseList)
  else:
    expenseList.append(expense)
    setExpenseList.append(expense)
    saveSetData(setExpenseList, variableExpenseList)


def addExpense():
  row = 4 +len(expenseList)
  name = input("Name of expense: ")
  value = int(input("Amount: "))
  expense = Expense(name, value, row, center)
  setOrNah(expense)
  expenseName = ctk.CTkLabel(center, text=name)
  expenseName.grid(row=row, column=1)
  expenseValue = ctk.CTkLabel(center, text=value)
  expenseValue.grid(row=row, column=2)
  

def saveSetData(setExpenseList, variableExpenseList):
  setExpenses = {}
  for expense in setExpenseList:
    setExpenses[expense.name] = expense.value
    
  variableExpenses = {}
  for item in variableExpenseList:
    variableExpenses[item.name] = item.value

  
  data = {
    "income": income,
    "Set Expenses": setExpenses,
    "Variable Expenses": variableExpenses
  }
  
  with open(setData, "w") as f:
    json.dump(data, f, indent=4)

#  Todo fix this function to grab values
def savings(currentValues):
  total = 0
  variableTotal = 0
  setTotal = 0
  for item in expenseList:
    # print(item.value)
    total = total + item.value
  # print(total)
  monthly = income * 4
  expectedSavings = monthly - total
  # print(expectedSavings)
  for item in currentValues:
    # print(item)
    variableTotal = int(item) + variableTotal
  # print(variableTotal)
  for item in setExpenseList:
    setTotal = item.value + setTotal
  # print(setTotal)
  actualTotal = setTotal + variableTotal
  # print(actualTotal)
  actualSavings = monthly - actualTotal
  # print(actualSavings)
  
  # messagebox.showinfo("Savings", f"Expected Savings: ${expectedSavings}\n\n Actual Savings: $ {actualSavings}" )
  
  return expectedSavings, actualSavings

def recordData(file, month, setExpenseList, variableExpenseList, currentValues, savingsData):
  with open(file, "a") as f:
    f.write(f"# {month}\n\n")
    f.write(f"---\n\n")
    f.write(f"###  Expenses\n\n")
    f.write(f"| Item | Expected | Actual |\n")
    f.write(f"| ---- | ---- | ---- |\n")
    for item in setExpenseList:
      f.write(f"| {item.name} | {item.value} | --- |\n")
    for item in variableExpenseList:
      f.write(f"| {item.name} | {item.value} | {item.actualValue.get()} |\n")
    f.write(f"### Savings this month\n")
    f.write(f"| Expected | Actual |\n")
    f.write(f"| --- | --- |\n")
    f.write(f"| {savingsData[0]} | {savingsData[1]} |\n\n")
    f.write(f"---\n")
    messagebox.showinfo("Success", f"Data has successfully been entered. Here is a summary of savings this round.\nExpected Savings: {savingsData[0]}\nActual Savings: {savingsData[1]}" )


def submitData():
  currentMonth = month.get()
  currentValues = []
  for item in variableExpenseList:
    currentValue = item.actualValue.get()
    currentValues.append(currentValue)
  savingsData = savings(currentValues)

  messagebox.showinfo("Saved", f"Data for {currentMonth} input")
  recordData(recordFile, currentMonth, setExpenseList, variableExpenseList, currentValues, savingsData)

add = ctk.CTkButton(buttonFrame, text="Add", command=addExpense)
add.grid(row=0,column=2, pady=5)
submit = ctk.CTkButton(buttonFrame, text="Submit", command=submitData)
submit.grid(row=1,column=2)

window.mainloop()
