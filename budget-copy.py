import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import json
import os

with open("config.json", "r") as configFile:
    config = json.load(configFile)

setData = config["setData"]
recordFile = config["recordFile"]

# Global state
expenseList = []
setExpenseList = []
variableExpenseList = []
bucketsList = []
income = 0

class Expense:
    def __init__(self, name, value, row, frame):
        self.name = name
        self.value = value
        self.label = ctk.CTkLabel(frame, text=name)
        self.label.grid(row=row, column=1)
        self.valueLabel = ctk.CTkLabel(frame, text=value)
        self.valueLabel.grid(row=row, column=2)

    def addActualEntry(self, frame, row):
        self.actualValue = ctk.CTkEntry(frame, placeholder_text=f"Actual {self.name}")
        self.actualValue.grid(row=row, column=3)

    def isVariable(self):
        return self.actualValue is not None
      
class Bucket:
    def __init__(self, name, total, percentage, frame=None):
        self.name = name
        self.percentage = percentage  # Percentage of savings
        self.total = total  # Accumulated total in this bucket
        self.goals = []
        self.label = ctk.CTkLabel(frame,text=name)
        self.label.pack(anchor="center",)
        self.percentageLabel = ctk.CTkLabel(frame, text=f"{self.percentage}%")
        self.percentageLabel.pack(anchor="center")
        self.totalLabel = ctk.CTkLabel(frame, text=f"Total: {self.total}")
        self.totalLabel.pack(after=self.label, anchor="center")

    def allocate(self, savingsAmount):
        """Add a portion of the savings to this bucket."""
        allocation = savingsAmount * (self.percentage / 100)
        self.total += allocation
        return allocation

    def addGoal(self, goal):
        self.goals.append(goal)


class Goal:
    def __init__(self, name, targetAmount, steps=None):
        self.name = name
        self.targetAmount = targetAmount
        self.steps = steps if steps else []  # Each step is a dict { "name": str, "amount": float, "complete": bool }
        self.allocatedAmount = 0.0

    def addStep(self, name, amount):
        self.steps.append({"name": name, "amount": amount, "complete": False})

    def allocateToGoal(self, amount):
        """Allocate savings to the goal."""
        self.allocatedAmount += amount

    def completeStep(self, stepIndex):
        if 0 <= stepIndex < len(self.steps):
            self.steps[stepIndex]["complete"] = True

    def isComplete(self):
        return self.allocatedAmount >= self.targetAmount

def loadJson(filePath):
    if os.path.exists(filePath):
        with open(filePath, "r") as file:
            return json.load(file)
    return {"income": 0, "SetExpenses": {}, "VariableExpenses": {}, "Buckets": []}

def saveData(setExpenseList, variableExpenseList, bucketsList):
    setExpenses = {exp.name: exp.value for exp in setExpenseList}
    variableExpenses = {exp.name: exp.value for exp in variableExpenseList}
    data = {
        "income": income,
        "SetExpenses": setExpenses,
        "VariableExpenses": variableExpenses,
        "Buckets": bucketsList
    }
    with open(setData, "w") as f:
        json.dump(data, f, indent=4)

def calculateSavings(currentValues):
    monthly = income * 4
    expectedTotal = sum(exp.value for exp in expenseList)
    expectedSavings = monthly - expectedTotal

    variableTotal = sum(int(val) for val in currentValues)
    setTotal = sum(exp.value for exp in setExpenseList)
    actualSavings = monthly - (variableTotal + setTotal)

    return expectedSavings, actualSavings

def recordDataToFile(monthValue, currentValues, savingsData):
    with open(recordFile, "a") as f:
        f.write(f"# {monthValue}\n\n---\n\n### Expenses\n\n")
        f.write("| Item | Expected | Actual |\n| ---- | ---- | ---- |\n")
        for exp in setExpenseList:
            f.write(f"| {exp.name} | {exp.value} | --- |\n")
        for i, exp in enumerate(variableExpenseList):
            f.write(f"| {exp.name} | {exp.value} | {currentValues[i]} |\n")
        f.write("\n### Savings this month\n")
        f.write("| Expected | Actual |\n| --- | --- |\n")
        f.write(f"| {savingsData[0]} | {savingsData[1]} |\n\n---\n")
        messagebox.showinfo("Success", f"Data recorded.\nExpected Savings: {savingsData[0]}\nActual Savings: {savingsData[1]}")

def submitData(monthEntry):
    currentMonth = monthEntry.get()
    currentValues = [exp.actualValue.get() for exp in variableExpenseList]
    savingsData = calculateSavings(currentValues)
    messagebox.showinfo("Saved", f"Data for {currentMonth} saved")
    recordDataToFile(currentMonth, currentValues, savingsData)

def deleteExpense():
    # Create a popup window
    modal = ctk.CTkToplevel()
    modal.title("Delete Expense")
    modal.geometry("350x200")

    # Dropdown of all expense names
    names = [expense.name for expense in expenseList]
    selectedName = ctk.StringVar(value=names[0] if names else "")

    dropdown = ctk.CTkOptionMenu(modal, values=names, variable=selectedName)
    dropdown.pack(pady=20)

    def applyDeletion():
        nameToDelete = selectedName.get()
        for expense in expenseList:
            if expense.name == nameToDelete:
                # Remove from UI
                expense.label.destroy()
                expense.valueLabel.destroy()
                if hasattr(expense, "actualValue"):
                    expense.actualValue.destroy()

                # Remove from lists
                expenseList.remove(expense)
                if expense in setExpenseList:
                    setExpenseList.remove(expense)
                elif expense in variableExpenseList:
                    variableExpenseList.remove(expense)

                # Save updates
                saveData(setExpenseList, variableExpenseList)

                messagebox.showinfo("Deleted", f"{nameToDelete} has been removed.")
                modal.destroy()
                return

    deleteBtn = ctk.CTkButton(modal, text="Delete", command=applyDeletion)
    deleteBtn.pack(pady=10)


def editExpense():
    # Create a popup window
    modal = ctk.CTkToplevel()
    modal.title("Edit Expense")
    modal.geometry("400x300")

    # Dropdown of current expenses
    names = [expense.name for expense in expenseList]
    selectedName = ctk.StringVar(value=names[0] if names else "")

    dropdown = ctk.CTkOptionMenu(modal, values=names, variable=selectedName)
    dropdown.pack(pady=10)

    nameEntry = ctk.CTkEntry(modal, placeholder_text="New name")
    nameEntry.pack(pady=10)

    valueEntry = ctk.CTkEntry(modal, placeholder_text="New value")
    valueEntry.pack(pady=10)

    def applyChanges():
        chosenName = selectedName.get()
        for expense in expenseList:
            if expense.name == chosenName:
                # Update values
                newName = nameEntry.get()
                newValue = valueEntry.get()

                if newName:
                    expense.name = newName
                    expense.label.configure(text=newName)

                if newValue:
                    try:
                        expense.value = int(newValue)
                        expense.valueLabel.configure(text=newValue)
                    except ValueError:
                        messagebox.showerror("Error", "Value must be a number.")
                        return

                saveData(setExpenseList, variableExpenseList)
                messagebox.showinfo("Success", "Expense updated successfully.")
                modal.destroy()
                return

    submitBtn = ctk.CTkButton(modal, text="Apply Changes", command=applyChanges)
    submitBtn.pack(pady=20)

def openAddExpenseModal(parentFrame):
    def confirmAdd():
        name = nameEntry.get()
        try:
            value = int(valueEntry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount must be a number")
            return

        isSet = setExpenseVar.get()
        row = 4 + len(expenseList)
        newExpense = Expense(name, value, row, parentFrame)
        expenseList.append(newExpense)
        if isSet:
            setExpenseList.append(newExpense)
        else:
            variableExpenseList.append(newExpense)
            newExpense.addActualEntry(parentFrame, row)
        saveData(setExpenseList, variableExpenseList)
        modal.destroy()

    modal = ctk.CTkToplevel()
    modal.title("Add Expense")
    modal.geometry("300x200")

    nameEntry = ctk.CTkEntry(modal, placeholder_text="Expense Name")
    nameEntry.pack(pady=5)
    valueEntry = ctk.CTkEntry(modal, placeholder_text="Amount")
    valueEntry.pack(pady=5)
    setExpenseVar = tk.BooleanVar()
    setCheck = ctk.CTkCheckBox(modal, text="Is this a set expense?", variable=setExpenseVar)
    setCheck.pack(pady=5)
    confirmButton = ctk.CTkButton(modal, text="Add Expense", command=confirmAdd)
    confirmButton.pack(pady=10)

def bucketWindow(buckets):
  bucketsWindow = ctk.CTkToplevel()
  bucketsWindow.title("Buckets")
  bucketsWindow.geometry("700x500")
  
  title = ctk.CTkLabel(bucketsWindow, text="Buckets")
  title.pack(anchor="center")
  
  centerFrame = ctk.CTkFrame(bucketsWindow)
  centerFrame.pack(anchor="center", pady=20, padx=20, fill="both", expand=True)
  # buttonFrame = ctk.CTkFrame(bucketsWindow)
  # buttonFrame.pack(pady=10)
  
  for name, value in buckets.items():
    print(f"Adding bucket: {name} Amount: {buckets[name]['Amount']} Percentage: {buckets[name]['Percentage']}")
    bucket = Bucket(name, buckets[name]["Amount"], buckets[name]["Percentage"],centerFrame)
    bucketsList.append(bucket)
  


def main():
    global income

    # Load data
    budget = loadJson(setData)
    income = budget["income"]
    buckets = budget["Buckets"]

    # Setup window
    ctk.set_appearance_mode("dark")
    window = ctk.CTk()
    window.title("Budget Calculator")
    window.geometry("700x500")
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)

    centerFrame = ctk.CTkFrame(window)
    centerFrame.grid(row=0, pady=20, padx=20)
    buttonFrame = ctk.CTkFrame(window)
    buttonFrame.grid(row=1, pady=10)

    # Add set expenses
    for name, value in budget["SetExpenses"].items():
        exp = Expense(name, value, row=4+len(expenseList), frame=centerFrame)
        expenseList.append(exp)
        setExpenseList.append(exp)

    # Add variable expenses
    for name, value in budget["VariableExpenses"].items():
        exp = Expense(name, value, row=4+len(expenseList), frame=centerFrame)
        exp.addActualEntry(centerFrame, 4+len(expenseList))
        expenseList.append(exp)
        variableExpenseList.append(exp)

    # Header UI
    ctk.CTkLabel(centerFrame, text="Budget Program").grid(row=0, column=2, pady=10)
    monthEntry = ctk.CTkEntry(centerFrame, placeholder_text="Month")
    monthEntry.grid(row=1, column=2)
    ctk.CTkLabel(centerFrame, text="Income:").grid(row=2, column=0)
    ctk.CTkLabel(centerFrame, text=str(income)).grid(row=2, column=1)
    ctk.CTkLabel(centerFrame, text="Expenses").grid(row=3, column=0, padx=10)
    ctk.CTkLabel(centerFrame, text="Actual Spending").grid(row=3, column=3)

    # Buttons
    ctk.CTkButton(buttonFrame, text="Add Expense", command=lambda: openAddExpenseModal(centerFrame)).grid(row=0, column=0, padx=10)
    ctk.CTkButton(buttonFrame, text="Submit", command=lambda: submitData(monthEntry)).grid(row=0, column=1, padx=10)
    ctk.CTkButton(buttonFrame, text="Edit Expense", command=editExpense).grid(row=0, column=2, padx=10)
    ctk.CTkButton(buttonFrame, text="Delete Expense", command=deleteExpense).grid(row=0, column=3, padx=10)
    ctk.CTkButton(buttonFrame, text="Buckets", command=lambda:bucketWindow(buckets)).grid(row=1, column=2, padx=10)

    window.mainloop()

if __name__ == "__main__":
    main()
