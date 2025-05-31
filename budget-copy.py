import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import json
import os

# TODO Add goals window and apply allocation and display for recording data

# Load configuration
with open("config.json", "r") as configFile:
    config = json.load(configFile)

SET_DATA_PATH = config["setData"]
RECORD_FILE_PATH = config["recordFile"]

# Global data
expenseList = []
setExpenseList = []
variableExpenseList = []
bucketsList = []
income = 0


# Expense class to represent an expense
class Expense:
    def __init__(self, name, value, row, frame):
        self.name = name
        self.value = value
        self.label = ctk.CTkLabel(frame, text=name)
        self.label.grid(row=row, column=1)
        self.valueLabel = ctk.CTkLabel(frame, text=value)
        self.valueLabel.grid(row=row, column=2)
        self.actualValue = None  # For variable expenses

    def addActualEntry(self, frame, row):
        self.actualValue = ctk.CTkEntry(frame, placeholder_text=f"Actual {self.name}")
        self.actualValue.grid(row=row, column=3)

    def isVariable(self):
        return self.actualValue is not None


# Bucket class for savings
class Bucket:
    def __init__(self, name, total, percentage, frame=None):
        self.name = name
        self.total = round(total, 3)
        self.percentage = percentage
        self.goals = []

        if frame:
            self.label = ctk.CTkLabel(frame, text=name)
            self.label.grid(row=4 + len(bucketsList), column=0, padx=10, pady=5)
            self.percentageLabel = ctk.CTkLabel(frame, text=f"{self.percentage}%")
            self.percentageLabel.grid(row=4 + len(bucketsList), column=1, padx=10, pady=5)
            self.totalLabel = ctk.CTkLabel(frame, text=f"{self.total}")
            self.totalLabel.grid(row=4 + len(bucketsList), column=2, padx=10, pady=5)

    def allocate(self, savingsAmount):
        allocation = savingsAmount * (self.percentage / 100)
        self.total += round(allocation, 3)
        return allocation

    def addGoal(self, goal):
        self.goals.append(goal)

    def toDict(self):
        return {
            "name": self.name,
            "Percentage": self.percentage,
            "Amount": self.total,
            "Goals": [goal.toDict() for goal in self.goals]
        }


# Goal class for each bucket
class Goal:
    def __init__(self, name, targetAmount, steps=None):
        self.name = name
        self.targetAmount = targetAmount
        self.steps = steps if steps else []
        self.allocatedAmount = 0.0

    def addStep(self, name, amount):
        self.steps.append({"name": name, "amount": amount, "complete": False})

    def allocateToGoal(self, amount):
        self.allocatedAmount += amount

    def completeStep(self, stepIndex):
        if 0 <= stepIndex < len(self.steps):
            self.steps[stepIndex]["complete"] = True

    def isComplete(self):
        return self.allocatedAmount >= self.targetAmount

    def toDict(self):
        return {
            "name": self.name,
            "targetAmount": self.targetAmount,
            "steps": self.steps,
            "allocatedAmount": self.allocatedAmount
        }


# Data helpers
def loadJson(filePath):
    if os.path.exists(filePath):
        with open(filePath, "r") as file:
            return json.load(file)
    return {"income": 0, "SetExpenses": {}, "VariableExpenses": {}, "Buckets": {}}


def saveData():
    setExpenses = {exp.name: exp.value for exp in setExpenseList}
    variableExpenses = {exp.name: exp.value for exp in variableExpenseList}
    bucketsDict = {bucket.name: {"Amount": bucket.total, "Percentage": bucket.percentage} for bucket in bucketsList}

    data = {
        "income": income,
        "SetExpenses": setExpenses,
        "VariableExpenses": variableExpenses,
        "Buckets": bucketsDict
    }
    with open(SET_DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)


def calculateSavings(currentValues):
    monthlyIncome = income * 4
    expectedTotal = sum(exp.value for exp in expenseList)
    expectedSavings = monthlyIncome - expectedTotal

    variableTotal = sum(int(val) for val in currentValues)
    setTotal = sum(exp.value for exp in setExpenseList)
    actualSavings = monthlyIncome - (variableTotal + setTotal)

    return expectedSavings, actualSavings


def recordDataToFile(monthValue, currentValues, savingsData):
    with open(RECORD_FILE_PATH, "a") as f:
        f.write(f"# {monthValue}\n\n---\n\n### Expenses\n\n")
        f.write("| Item | Expected | Actual |\n| ---- | ---- | ---- |\n")
        for exp in setExpenseList:
            f.write(f"| {exp.name} | {exp.value} | --- |\n")
        for i, exp in enumerate(variableExpenseList):
            f.write(f"| {exp.name} | {exp.value} | {currentValues[i]} |\n")
        f.write("\n### Savings this month\n")
        f.write("| Expected | Actual |\n| --- | --- |\n")
        f.write(f"| {savingsData[0]} | {savingsData[1]} |\n\n")
        f.write("---\n\n### Accounts this month\n")
        f.write("| Name | Amount | % |\n| --- | --- | --- |\n")
        for bucket in bucketsList:
            f.write(f"| {bucket.name} | {bucket.total} | {bucket.percentage} |\n")
    messagebox.showinfo("Success", f"Data recorded.\nExpected Savings: {savingsData[0]}\nActual Savings: {savingsData[1]}")


# Core functions
def submitData(monthEntry):
    currentMonth = monthEntry.get()
    currentValues = [exp.actualValue.get() if exp.actualValue else "0" for exp in variableExpenseList]

    savingsData = calculateSavings(currentValues)

    # Allocate savings to buckets
    for bucket in bucketsList:
        previousTotal = bucket.total
        allocation = bucket.allocate(savingsData[1])
        messagebox.showinfo(bucket.name, f"Previous Total: {previousTotal}\nNew Total: {bucket.total}\nAllocated: {allocation}")

    saveData()
    recordDataToFile(currentMonth, currentValues, savingsData)
    messagebox.showinfo("Saved", f"Data for {currentMonth} saved and allocated.")


def deleteExpense():
    modal = ctk.CTkToplevel()
    modal.title("Delete Expense")
    modal.geometry("350x200")

    names = [expense.name for expense in expenseList]
    selectedName = ctk.StringVar(value=names[0] if names else "")

    dropdown = ctk.CTkOptionMenu(modal, values=names, variable=selectedName)
    dropdown.pack(pady=20)

    def applyDeletion():
        nameToDelete = selectedName.get()
        for expense in expenseList:
            if expense.name == nameToDelete:
                expense.label.destroy()
                expense.valueLabel.destroy()
                if expense.actualValue:
                    expense.actualValue.destroy()
                expenseList.remove(expense)
                if expense in setExpenseList:
                    setExpenseList.remove(expense)
                elif expense in variableExpenseList:
                    variableExpenseList.remove(expense)
                saveData()
                messagebox.showinfo("Deleted", f"{nameToDelete} has been removed.")
                modal.destroy()
                return

    deleteBtn = ctk.CTkButton(modal, text="Delete", command=applyDeletion)
    deleteBtn.pack(pady=10)


def editExpense():
    modal = ctk.CTkToplevel()
    modal.title("Edit Expense")
    modal.geometry("400x300")

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
                saveData()
                messagebox.showinfo("Success", "Expense updated successfully.")
                modal.destroy()
                return

    submitBtn = ctk.CTkButton(modal, text="Apply Changes", command=applyChanges)
    submitBtn.pack(pady=20)


def openAddExpenseModal(parentFrame):
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

    def confirmAdd():
        name = nameEntry.get()
        try:
            value = int(valueEntry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount must be a number")
            return
        row = 4 + len(expenseList)
        newExpense = Expense(name, value, row, parentFrame)
        expenseList.append(newExpense)
        if setExpenseVar.get():
            setExpenseList.append(newExpense)
        else:
            variableExpenseList.append(newExpense)
            newExpense.addActualEntry(parentFrame, row)
        saveData()
        modal.destroy()

    confirmButton = ctk.CTkButton(modal, text="Add Expense", command=confirmAdd)
    confirmButton.pack(pady=10)


def bucketWindow(buckets):
    bucketsWindow = ctk.CTkToplevel()
    bucketsWindow.title("Buckets")
    bucketsWindow.geometry("700x500")

    ctk.CTkLabel(bucketsWindow, text="Buckets").pack(anchor="center")
    centerFrame = ctk.CTkFrame(bucketsWindow)
    centerFrame.pack(anchor="center", pady=20, padx=20, fill="both", expand=True)
    ctk.CTkLabel(centerFrame, text="Bucket").grid(row=0, column=0, padx=10, pady=5)
    ctk.CTkLabel(centerFrame, text="Portion (%)").grid(row=0, column=1, padx=10, pady=5)
    ctk.CTkLabel(centerFrame, text="Total").grid(row=0, column=2, padx=10, pady=5)

    for name, data in buckets.items():
        bucket = Bucket(name, data["Amount"], data["Percentage"], centerFrame)
        bucketsList.append(bucket)

    def editBuckets():
        modal = ctk.CTkToplevel()
        modal.title("Edit Buckets")
        modal.geometry("400x300")

        names = [bucket.name for bucket in bucketsList]
        selectedName = ctk.StringVar(value=names[0] if names else "")

        dropdown = ctk.CTkOptionMenu(modal, values=names, variable=selectedName)
        dropdown.pack(pady=10)
        percentageEntry = ctk.CTkEntry(modal, placeholder_text="New Percentage")
        percentageEntry.pack(pady=10)
        totalEntry = ctk.CTkEntry(modal, placeholder_text="New Total")
        totalEntry.pack(pady=10)

        def applyChanges():
            chosenName = selectedName.get()
            for bucket in bucketsList:
                if bucket.name == chosenName:
                    newPercentage = percentageEntry.get()
                    newTotal = totalEntry.get()
                    if newPercentage:
                        try:
                            bucket.percentage = float(newPercentage)
                            bucket.percentageLabel.configure(text=f"{newPercentage}%")
                        except ValueError:
                            messagebox.showerror("Error", "Percentage must be a number.")
                            return
                    if newTotal:
                        try:
                            bucket.total = float(newTotal)
                            bucket.totalLabel.configure(text=f"{newTotal}")
                        except ValueError:
                            messagebox.showerror("Error", "Total must be a number.")
                            return
                    saveData()
                    messagebox.showinfo("Success", "Bucket updated successfully.")
                    modal.destroy()
                    return

        ctk.CTkButton(modal, text="Save", command=applyChanges).pack(pady=10)

    ctk.CTkButton(centerFrame, text="Edit Buckets", command=editBuckets).grid(row=5 + len(bucketsList), column=3, padx=10, pady=5)


def main():
    global income

    # Load initial data
    budget = loadJson(SET_DATA_PATH)
    income = budget["income"]
    buckets = budget["Buckets"]

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

    # Load expenses
    for name, value in budget["SetExpenses"].items():
        row = 4 + len(expenseList)
        exp = Expense(name, value, row, centerFrame)
        expenseList.append(exp)
        setExpenseList.append(exp)

    for name, value in budget["VariableExpenses"].items():
        row = 4 + len(expenseList)
        exp = Expense(name, value, row, centerFrame)
        exp.addActualEntry(centerFrame, row)
        expenseList.append(exp)
        variableExpenseList.append(exp)

    # Month entry
    monthEntry = ctk.CTkEntry(buttonFrame, placeholder_text="Enter month")
    monthEntry.pack(pady=5)

    # Buttons
    ctk.CTkButton(buttonFrame, text="Submit Data", command=lambda: submitData(monthEntry)).pack(pady=5)
    ctk.CTkButton(buttonFrame, text="Add Expense", command=lambda: openAddExpenseModal(centerFrame)).pack(pady=5)
    ctk.CTkButton(buttonFrame, text="Edit Expense", command=editExpense).pack(pady=5)
    ctk.CTkButton(buttonFrame, text="Delete Expense", command=deleteExpense).pack(pady=5)
    ctk.CTkButton(buttonFrame, text="View Buckets", command=lambda: bucketWindow(buckets)).pack(pady=5)

    window.mainloop()


if __name__ == "__main__":
    main()
