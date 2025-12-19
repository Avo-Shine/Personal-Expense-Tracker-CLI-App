
#Function to safely convert user input into a number
def parse_amount(raw):
    try:
        amt = float(raw)
        if amt < 0:
            raise ValueError("Amount must be non-negative.")
        return amt
    except ValueError:
        #If conversion fails, raise an error
        raise ValueError("Please enter a valid number for amount") 
    
#Function to format numbers as currency 
def format_currency(amt):
    return f"{amt: .2f}"