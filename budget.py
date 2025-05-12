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

# Function to load income and expenses data from the JSON file
def loadData(file):
    if os.path.exists(file):  # Check if the file exists
        with open(file, "r") as file:
            return json.load(file)  # Load and return the JSON data as a Python dictionary
    return {"income": 0, "expenses": {}}  # Return default structure if file doesn't exist

# Load the budget data from the file
budget = loadData(setData)

# Extract the income and expenses from the loaded data
income = budget["income"]
expenses = budget["expenses"]
rent = expenses["rent"]
electric = expenses["electric"]
food = expenses["food"]
weed = expenses["weed"]
youtube = expenses["youtube"]
wifi = expenses["wifi"]

ctk.set_appearance_mode("dark")
window = ctk.CTk()
window.title("Budget Calculator")
window.geometry("1500 x 1500")

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

center = ctk.CTkFrame(window)
center.grid(row=0, pady=20, padx=20)
buttonFrame = ctk.CTkFrame(window)
buttonFrame.grid(row=1, sticky="ew", pady=10)

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

# Rent
rentExpense = ctk.CTkLabel(center, text="Rent")
rentExpense.grid(row=4, column=1)
rentData = ctk.CTkLabel(center, text=rent)
rentData.grid(row=4, column=2)

# Electric
electricExpense = ctk.CTkLabel(center, text="Electric")
electricExpense.grid(row=5, column=1)
electricData = ctk.CTkLabel(center, text=electric)
electricData.grid(row=5, column=2)

# Food
foodExpense = ctk.CTkLabel(center, text="Food")
foodExpense.grid(row=6, column=1)
foodData = ctk.CTkLabel(center, text=food)
foodData.grid(row=6, column=2)

# Weed
weedExpense = ctk.CTkLabel(center, text="Weed")
weedExpense.grid(row=7, column=1)
weedData = ctk.CTkLabel(center, text=weed)
weedData.grid(row=7, column=2)

# YouTube
youtubeExpense = ctk.CTkLabel(center, text="YouTube")
youtubeExpense.grid(row=8, column=1)
youtubeData = ctk.CTkLabel(center, text=youtube)
youtubeData.grid(row=8, column=2)

# WiFi
wifiExpense = ctk.CTkLabel(center, text="WiFi")
wifiExpense.grid(row=9, column=1)
wifiData = ctk.CTkLabel(center, text=wifi)
wifiData.grid(row=9, column=2)

actual = ctk.CTkLabel(center, text="Actual Spending")
actual.grid(row=3, column=4)
actualElectric = ctk.CTkEntry(center, placeholder_text="Electric")
actualElectric.grid(row=5, column=4)

actualFood = ctk.CTkEntry(center, placeholder_text="Food")
actualFood.grid(row=6, column=4)

actualWeed = ctk.CTkEntry(center, placeholder_text="Weed")
actualWeed.grid(row=7, column=4)

def saveData(month, actualElectric, actualFood, actualWeed,expectedSavings, actualSavings ):
    data = {
      "month": month,
      "actual": {
        "electric": actualElectric,
        "food": actualFood,
        "weed": actualWeed,
      },
      "savings": {
        "expected": expectedSavings,
        "actual": actualSavings,
      }
      }
    
    with open(outputFile, "a") as f:
        json.dump(data, f, indent=4)  # Indented for readability
        

def savings(actualFood,actualElectric,actualWeed):
  expenses = rent + electric + food + weed + wifi + youtube
  monthly = income * 4
  expectedSavings = monthly - expenses
  actualExpenses = rent + actualElectric + actualFood + actualWeed + wifi + youtube
  actualSavings = monthly - actualExpenses
  messagebox.showinfo("Savings", f"Expected Savings: ${expectedSavings}\n\n Actual Savings: $ {actualSavings}" )
  
  return expectedSavings, actualSavings

def submitData():
  currentMonth = month.get()
  currentElectric = float(actualElectric.get())
  currentFood = float(actualFood.get())
  currentWeed = float(actualWeed.get())
  
  savingsData = savings(currentFood, currentElectric, currentWeed)

  saveData(currentMonth, currentElectric, currentFood, currentWeed, savingsData[0], savingsData[1])
  messagebox.showinfo("Saved", f"Data for {currentMonth} input")

submit = ctk.CTkButton(buttonFrame, text="Submit", command=submitData)
submit.grid(row=0,column=1, padx=150)

window.mainloop()
