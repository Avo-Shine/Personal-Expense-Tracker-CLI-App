
# Define a class called Expense to represent a single record 
class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
    
    #Method called summary will return a formatted stringof the expense details
    def summary(self):
        return f"{self.date} | {self.category} | {self.amount: .2f} | {self.description}"