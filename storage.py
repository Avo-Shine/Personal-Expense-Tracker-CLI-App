
import json
from pathlib import Path
from expense import Expense 

#Define the file where expenses will be stored
DATA_FILE = Path("data.json")

#Function to load expenses from the JSON file 
def load_expenses():
    #if the file doesn't exist yet, return an empty list 
    if not DATA_FILE.exists():
        return []
    
    #Open the file and read its content 
    with DATA_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)
    
    #Convert each dictionary back into an Expense object
    return [Expense(**item) for item in data]

#Function to save expenses to the JSON file
def save_expenses(expenses):
    #open the file in write mode
    with DATA_FILE.open("w", encoding="utf-8") as f:
        #convert each Expense object into a dictionary before saving
        json.dump([e.__dict__ for e in expenses], f, indent=4)