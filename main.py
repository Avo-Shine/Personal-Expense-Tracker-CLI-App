from storage import load_expenses, save_expenses
from expense import Expense
from utils import parse_amount, format_currency

#function to display the menu
def show_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter by Category")
    print("4. Show total spent")
    print("5. Quit")

#function to add a new expense
def add_expense(expenses):
    try:
        amount = parse_amount(input("Amount: ").strip())
        category = input("Category: ").strip() or "General"
        description = input("Description: ").strip() or "-"
        date = input("Date (YYYY-MM-DD): ").strip() or "2025-12-19"

        #create a new Expense object
        e = Expense(amount, category, description, date)
        expenses.append(e)
        save_expenses(expenses)
        print("Expense saved successfully!")
    except ValueError as e:
        print(f"Error: {e}")

# Function to view all expenses
def view_all(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e.summary()}")

# Function to filter expenses by category
def filter_by_category(expenses):
    q = input("Category to filter: ").strip()
    filtered = [e for e in expenses if e.category.lower() == q.lower()]
    if not filtered:
        print("No matches found.")
        return
    for i, e in enumerate(filtered, start=1):
        print(f"{i}. {e.summary()}")

# Function to calculate total spent
def total_spent(expenses):
    total = sum(e.amount for e in expenses)
    print(f"Total spent: {format_currency(total)}")

# Main loop
def main():
    expenses = load_expenses()
    while True:
        show_menu()
        choice = input("Choose (1-5): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_all(expenses)
        elif choice == "3":
            filter_by_category(expenses)
        elif choice == "4":
            total_spent(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()