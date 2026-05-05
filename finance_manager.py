import csv
import os
from datetime import datetime

FILE_NAME = "transactions.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount", "Description"])

def add_transaction():
    trans_type = input("Type (Income/Expense): ").capitalize()
    if trans_type not in ["Income", "Expense"]:
        print("Invalid type. Use Income or Expense.")
        return

    category = input("Category: ")
    try:
        amount = float(input("Amount: ₹"))
    except ValueError:
        print("Invalid amount.")
        return
    description = input("Description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, trans_type, category, amount, description])
    print("Transaction added successfully.")

def view_balance():
    income = 0
    expense = 0
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Type"] == "Income":
                    income += float(row["Amount"])
                elif row["Type"] == "Expense":
                    expense += float(row["Amount"])
    except FileNotFoundError:
        print("No transactions found.")
        return

    balance = income - expense
    print(f"\nTotal Income: ₹{income:.2f}")
    print(f"Total Expense: ₹{expense:.2f}")
    print(f"Current Balance: ₹{balance:.2f}\n")

def view_transactions():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            print("\n--- All Transactions ---")
            for row in reader:
                print(" | ".join(row))
            print()
    except FileNotFoundError:
        print("No transactions found.")

def category_summary():
    categories = {}
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cat = row["Category"]
                amt = float(row["Amount"])
                if row["Type"] == "Expense":
                    categories[cat] = categories.get(cat, 0) + amt
    except FileNotFoundError:
        print("No transactions found.")
        return

    print("\n--- Expense by Category ---")
    for cat, total in categories.items():
        print(f"{cat}: ₹{total:.2f}")
    print()

def main():
    init_file()
    while True:
        print("=== Personal Finance Manager ===")
        print("1. Add Transaction")
        print("2. View Balance")
        print("3. View All Transactions")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_balance()
        elif choice == '3':
            view_transactions()
        elif choice == '4':
            category_summary()
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()