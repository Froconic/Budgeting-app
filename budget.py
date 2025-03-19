import tkinter as tk
import json
import os

file = "data.json"

def grabData(file):
  with open(file, "w+") as f:
    print(file)