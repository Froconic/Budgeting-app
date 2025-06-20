import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import customtkinter as ctk
import json
import os

# Add a way to change income then all thats left is theming and fonts

def configuration():
  config = "config.json"
  
  if os.path.exists(config):
    with open(config, "r") as configFile:
        return json.load(configFile)

  root = tk.Tk()
  root.withdraw()  # Hide the root window
  messagebox.showinfo("Setup", "Please select the path to your Set Data file.")
  setDataPath = filedialog.askdirectory(title="Select Set Data Directory")
  setDataFile = setDataPath + "/setData.json"
  # setDataFile = os.path.join(setDataPath, "setData.json")

  messagebox.showinfo("Setup", "Please select the path to your Record file.")
  recordFilePath = filedialog.askdirectory(title="Select Record File Directory")
  recordFile = recordFilePath + "/Budget.md"
  # recordFile = os.path.join(recordFilePath, "record.md")
  
  configData = {
      "setData": setDataFile,
      "recordFile": recordFile
  }

  # Also create empty files if they don't exist
  if not os.path.exists(setDataFile):
    income = simpledialog.askinteger("Income", "Please enter your weekly income:")
    with open(setDataFile, "w") as f:
      json.dump({
        "income": income,
        "SetExpenses": {},
        "VariableExpenses": {},
        "Buckets": {},
        "Goals": {}
      }, f, indent=4)

  if not os.path.exists(recordFile):
    with open(recordFile, "w") as f:
      f.write("# Expense Records\n\n")

  configData = {
      "setData": setDataFile,
      "recordFile": recordFile
  }

    # Load configuration
  with open(config, "w") as configFile:
      config = json.dump(configData, configFile, indent=4)

  
  return configData

config = configuration()
SET_DATA_PATH = config["setData"]
RECORD_FILE_PATH = config["recordFile"]

# Global data
expenseList = []
setExpenseList = []
variableExpenseList = []
bucketsList = []
goalsList = []
income = 0


# Expense class to represent an expense
class Expense:
    def __init__(self, name, value, row, frame):
        self.name = name
        self.value = value
        self.label = ctk.CTkLabel(frame, text=name)
        self.label.grid(row=row, column=1, padx=10, pady=5)
        self.valueLabel = ctk.CTkLabel(frame, text=value)
        self.valueLabel.grid(row=row, column=2, padx=10)
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

    def toDict(self):
        return {
            "name": self.name,
            "Percentage": self.percentage,
            "Amount": self.total,
        }


# Goal class for each bucket
class Goal:
    def __init__(self, name, target, currentAmount, frame=None):
        self.name = name
        self.target = round(target, 3)
        self.currentAmount = currentAmount
        
        if frame:
            self.label = ctk.CTkLabel(frame, text=name)
            self.label.grid(row=4 + len(goalsList), column=0, padx=10, pady=5)
            self.targetLabel = ctk.CTkLabel(frame, text=f"Target: {self.target}")
            self.targetLabel.grid(row=4 + len(goalsList), column=1, padx=10, pady=5)
            self.currentLabel = ctk.CTkLabel(frame, text=f"Allocated: {self.currentAmount}")
            self.currentLabel.grid(row=4 + len(goalsList), column=2, padx=10, pady=5)

    def allocateToGoal(self, amount):
        self.currentAmount += round(amount, 3)

    def isComplete(self):
        return self.currentAmount >= self.target

    def toDict(self):
        return {
            "name": self.name,
            "target": self.target,
            "currentAmount": self.currentAmount
        }


# Data helpers
def loadJson(filePath):
    if os.path.exists(filePath):
        with open(filePath, "r") as file:
            return json.load(file)
    return {"income": 0, "SetExpenses": {}, "VariableExpenses": {}, "Buckets": {}, "Goals": {}}


def saveData():
    setExpenses = {exp.name: exp.value for exp in setExpenseList}
    variableExpenses = {exp.name: exp.value for exp in variableExpenseList}
    bucketsDict = {bucket.name: {"Amount": bucket.total, "Percentage": bucket.percentage} for bucket in bucketsList}
    goalsDict = {goal.name: {"Target": goal.target, "Current Amount": goal.currentAmount} for goal in goalsList}

    data = {
        "income": income,
        "SetExpenses": setExpenses,
        "VariableExpenses": variableExpenses,
        "Buckets": bucketsDict,
        "Goals": goalsDict
    }
    with open(SET_DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)


def calculateSavings(currentValues):
    monthlyIncome = income * 4
    expectedTotal = sum(exp.value for exp in expenseList)
    expectedSavings = monthlyIncome - expectedTotal

    variableTotal = sum(float(val) for val in currentValues)
    setTotal = sum(exp.value for exp in setExpenseList)
    actualSavings = round(monthlyIncome - (variableTotal + setTotal), 3)

    return expectedSavings, actualSavings


def recordDataToFile(monthValue, currentValues, savingsData, buckets):
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
        for name, data in buckets.items():
            f.write(f"| {name} | {data['Amount']} | {data['Percentage']} |\n")
        f.write("\n---\n\n")
    messagebox.showinfo("Success", f"Data recorded.\nExpected Savings: {savingsData[0]}\nActual Savings: {savingsData[1]}")


# Core functions
def submitData(monthEntry):
    budget = loadJson(SET_DATA_PATH)
    buckets = budget["Buckets"]
    currentMonth = monthEntry.get()
    currentValues = [round(float(exp.actualValue.get()), 3) if exp.actualValue else "0" for exp in variableExpenseList]

    savingsData = calculateSavings(currentValues)

    # Allocate savings to buckets
    messagebox.showinfo("Allocation", "Allocation will commence")
    for bucket in bucketsList:
        previousTotal = round(bucket.total, 3)
        allocation = round(bucket.allocate(savingsData[1]),3)
        messagebox.showinfo(bucket.name, f"Previous Total: {previousTotal}\nNew Total: {bucket.total}\nAllocated: {allocation}")

    recordDataToFile(currentMonth, currentValues, savingsData, buckets)
    saveData()
    messagebox.showinfo("Saved", f"Data for {currentMonth} saved and recorded.")


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
                        expense.value = float(newValue)
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
            value = float(valueEntry.get())
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

# Add a way to add buckets
def bucketWindow(buckets):
    bucketsWindow = ctk.CTkToplevel()
    bucketsWindow.title("Buckets")
    bucketsWindow.geometry("400x400")

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

    def addBucket():
        bucketModal = ctk.CTkToplevel()
        bucketModal.title("Add Bucket")
        bucketModal.geometry("300x200")

        nameEntry = ctk.CTkEntry(bucketModal, placeholder_text="Bucket Name")
        nameEntry.pack(pady=5)
        percentageEntry = ctk.CTkEntry(bucketModal, placeholder_text="Percentage")
        percentageEntry.pack(pady=5)
        totalEntry = ctk.CTkEntry(bucketModal, placeholder_text="Total Amount")
        totalEntry.pack(pady=5)

        def confirmAddBucket():
            bucketName = nameEntry.get()
            try:
                percentage = float(percentageEntry.get())
                total = float(totalEntry.get())
                newBucket = Bucket(bucketName, total, percentage, centerFrame)
                bucketsList.append(newBucket)
                saveData()
                bucketModal.destroy()
            except ValueError:
                messagebox.showerror("Invalid Input", "Percentage and Total must be numbers")

        ctk.CTkButton(bucketModal, text="Confirm", command=confirmAddBucket).pack(pady=10)
    def deleteBucket():
        modal = ctk.CTkToplevel()
        modal.title("Delete Bucket")
        modal.geometry("400x200")

        names = [bucket.name for bucket in bucketsList]
        selectedName = ctk.StringVar(value=names[0] if names else "")

        dropdown = ctk.CTkOptionMenu(modal, values=names, variable=selectedName)
        dropdown.pack(pady=10)

        def confirmDelete():
            chosenName = selectedName.get()
            for bucket in bucketsList:
                if bucket.name == chosenName:
                    bucket.label.destroy()
                    bucket.percentageLabel.destroy()
                    bucket.totalLabel.destroy()
                    bucketsList.remove(bucket)
                    saveData()
                    messagebox.showinfo("Deleted", f"{chosenName} has been deleted.")
                    modal.destroy()
                    return

        ctk.CTkButton(modal, text="Delete", command=confirmDelete).pack(pady=10)

    ctk.CTkButton(centerFrame, text="Edit Buckets", command=editBuckets).grid(row=5 + len(bucketsList), column=1, padx=10, pady=5)
    ctk.CTkButton(centerFrame, text="Add Bucket", command=addBucket).grid(row=6 + len(bucketsList), column=1, padx=10, pady=5)
    ctk.CTkButton(centerFrame, text="Delete Bucket", command=deleteBucket).grid(row=7 + len(bucketsList), column=1, padx=10, pady=5)

def goalsWindow(goals):
  modal = ctk.CTkToplevel()
  modal.title(f"Goals")
  modal.geometry("400x500")
  
  ctk.CTkLabel(modal, text=f"Goals").pack(anchor="center", pady=10)
  centerFrame = ctk.CTkFrame(modal)
  centerFrame.pack(anchor="center", pady=20, padx=20, fill="both", expand=True)
  
  for name, data in goals.items():
      goal = Goal(name, data["Target"], data["Current Amount"], centerFrame)
      goalsList.append(goal)
  
  def editGoals():
    modal = ctk.CTkToplevel()
    modal.title("Edit Goals")
    modal.geometry("400x300")
    
    names = [goal.name for goal in goalsList]
    selectedName = ctk.StringVar(value=names[0] if names else "")
    
    dropdown = ctk.CTkOptionMenu(modal, values=names, variable=selectedName)
    dropdown.pack(pady=10)
    
    targetEntry = ctk.CTkEntry(modal, placeholder_text="New Target Amount")
    targetEntry.pack(pady=10)
    currentEntry = ctk.CTkEntry(modal, placeholder_text="New Allocated Amount")
    currentEntry.pack(pady=10)
    
    def applyChanges():
        chosenName = selectedName.get()
        for goal in goalsList:
            if goal.name == chosenName:
                newAllocated = currentEntry.get()
                newTarget = targetEntry.get()
                if newAllocated:
                    try:
                        goal.currentAmount = float(newAllocated)
                        goal.currentLabel.configure(text=f"Allocated: {goal.currentAmount}")
                    except ValueError:
                        messagebox.showerror("Error", "Allocated amount must be a number.")
                        return
                if newTarget:
                    try:
                        goal.target = float(newTarget)
                        goal.targetLabel.configure(text=f"Target: {goal.target}")
                    except ValueError:
                        messagebox.showerror("Error", "Target must be a number.")
                        return
                saveData()
                messagebox.showinfo("Success", "Goal updated successfully.")
                modal.destroy()
                return
    ctk.CTkButton(modal, text="Save", command=applyChanges).pack(pady=10)
    
  def allocateToGoal():
    modal = ctk.CTkToplevel()
    modal.title("Allocate to Goal")
    modal.geometry("400x200")

    names = [goal.name for goal in goalsList]
    selectedName = ctk.StringVar(value=names[0] if names else "")

    dropdown = ctk.CTkOptionMenu(modal, values=names, variable=selectedName)
    dropdown.pack(pady=10)

    amountEntry = ctk.CTkEntry(modal, placeholder_text="Amount to allocate")
    amountEntry.pack(pady=10)

    def applyAllocation():
        chosenName = selectedName.get()
        try:
            amount = float(amountEntry.get())
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return

        for goal in goalsList:
            if goal.name == chosenName:
                goal.allocateToGoal(amount)
                goal.currentLabel.configure(text=f"Allocated: {goal.currentAmount}")
                saveData()
                messagebox.showinfo("Success", f"Allocated {amount} to {goal.name}.")
                modal.destroy()
                return

    ctk.CTkButton(modal, text="Allocate", command=applyAllocation).pack(pady=10)
  
  def addGoal():
    goalModal = ctk.CTkToplevel()
    goalModal.title("Add Goal")
    goalModal.geometry("300x200")
    
    nameEntry = ctk.CTkEntry(goalModal, placeholder_text="Goal Name")
    nameEntry.pack(pady=5)
    targetEntry = ctk.CTkEntry(goalModal, placeholder_text="Target Amount")
    targetEntry.pack(pady=5)
    ctk.CTkButton(goalModal, text="Confirm", command=lambda: confirmAddGoal()).pack(pady=10)
    
    def confirmAddGoal():
      goalName = nameEntry.get()
      try:
          targetAmount = float(targetEntry.get())
          newGoal = Goal(goalName, targetAmount, currentAmount=0, frame=centerFrame)
          goalsList.append(newGoal)
          saveData()
          goalModal.destroy()
      except ValueError:
          messagebox.showerror("Invalid Input", "Target amount must be a number")

  def deleteGoal():
    modal = ctk.CTkToplevel()
    modal.title("Delete Goal")
    modal.geometry("400x200")

    names = [goal.name for goal in goalsList]
    selectedName = ctk.StringVar(value=names[0] if names else "")

    dropdown = ctk.CTkOptionMenu(modal, values=names, variable=selectedName)
    dropdown.pack(pady=10)

    def confirmDelete():
        chosenName = selectedName.get()
        for goal in goalsList:
            if goal.name == chosenName:
                goal.label.destroy()
                goal.targetLabel.destroy()
                goal.currentLabel.destroy()
                goalsList.remove(goal)
                saveData()
                messagebox.showinfo("Deleted", f"{chosenName} has been deleted.")
                modal.destroy()
                return

    ctk.CTkButton(modal, text="Delete", command=confirmDelete).pack(pady=10)

  ctk.CTkButton(modal, text="Add Goal", command=addGoal).pack(pady=10)
  ctk.CTkButton(modal, text="Edit Goals", command=editGoals).pack(pady=10)
  ctk.CTkButton(modal, text="Allocate to Goal", command=allocateToGoal).pack(pady=10)
  ctk.CTkButton(modal, text="Delete Goal", command=deleteGoal).pack(pady=10)
  ctk.CTkButton(modal, text="Save", command=saveData).pack(pady=10)


def main():
    global income

    # Load initial data
    budget = loadJson(SET_DATA_PATH)
    income = budget["income"]
    buckets = budget["Buckets"]
    goals = budget["Goals"]

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    window = ctk.CTk()
    window.iconbitmap("C:/Users/akira/Desktop/Stuff/Code/GitHub/Budgeting-app/dist/budget/_internal/budget.py/assets/icons/CustomTkinter_icon_Windows.ico")
    window.title("Budget Calculator")
    window.geometry("400x700")
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)

    centerFrame = ctk.CTkFrame(window)
    centerFrame.grid(row=0, pady=20, padx=20, ipadx=20, ipady=20)
    buttonFrame = ctk.CTkFrame(window)
    buttonFrame.grid(row=1, pady=10)
    
    titleLabel = ctk.CTkLabel(centerFrame, text="Expenses", font=("JetBrains Mono", 24))
    titleLabel.grid(row=0, column=3, pady=10)

    # Month entry
    monthEntry = ctk.CTkEntry(centerFrame, placeholder_text="Enter month")
    monthEntry.grid(row=1, column=3, padx=10, pady=5)

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
    
    for name, data in buckets.items():
        bucket = Bucket(name, data["Amount"], data["Percentage"], frame = None)
        bucketsList.append(bucket)

    # Buttons
    ctk.CTkButton(buttonFrame, text="Submit Data", command=lambda: submitData(monthEntry)).pack(pady=5)
    ctk.CTkButton(buttonFrame, text="Add Expense", command=lambda: openAddExpenseModal(centerFrame)).pack(pady=5)
    ctk.CTkButton(buttonFrame, text="Edit Expense", command=editExpense).pack(pady=5)
    ctk.CTkButton(buttonFrame, text="Delete Expense", command=deleteExpense).pack(pady=5)
    ctk.CTkButton(buttonFrame, text="View Buckets", command=lambda: bucketWindow(buckets)).pack(pady=5)
    ctk.CTkButton(buttonFrame, text="Open Goals", command=lambda: goalsWindow(goals)).pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    main()
