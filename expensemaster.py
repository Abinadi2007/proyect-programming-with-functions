#Copyright 2024 Joseph Abinadi Jimenez Davis, BYU Student, proyect for course "Programming with functions"

import csv
import os

DIRECTORY = r'C:\Users\wonde\OneDrive\Documentos\BYU-PYTHON\week 5' # You can edit this if you got troubles loading the files

class Expense:
    def __init__(self, date, amount, category):
        self.date = date
        self.amount = amount
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def generate_report(self):
        # Generate and display reports
        pass

    def export_data(self, format):
        if format.lower() == "csv":
            self.export_to_csv()
        elif format.lower() == "txt":
            self.export_to_txt()
        else:
            print("Unsupported format. Please choose CSV or TXT.")

    def export_to_csv(self):
        csv_file_path = os.path.join(DIRECTORY, 'expenses.csv')
        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = ['Date', 'Amount', 'Category']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for expense in self.expenses:
                writer.writerow({'Date': expense.date, 'Amount': expense.amount, 'Category': expense.category})
        print("Data exported to expenses.csv successfully!")

    def export_to_txt(self):
        txt_file_path = os.path.join(DIRECTORY, 'expense_data.txt')
        with open(txt_file_path, 'w') as txtfile:
            txtfile.write("Date       Amount   Category\n")
            for expense in self.expenses:
                txtfile.write(f"{expense.date} {expense.amount:>8}   {expense.category}\n")
        print("Data exported to expense_data.txt successfully!")

    def load_expenses_csv(self, filename):
        csv_file_path = os.path.join(DIRECTORY, filename)
        try:
            with open(csv_file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    expense = Expense(row['Date'], float(row['Amount']), row['Category'])
                    self.expenses.append(expense)
            print("Expenses loaded successfully from", filename)
        except FileNotFoundError:
            print(f"File {filename} not found in directory {DIRECTORY}.")

    def load_expenses_txt(self, filename):
        txt_file_path = os.path.join(DIRECTORY, filename)
        try:
            with open(txt_file_path, 'r') as txtfile:
                next(txtfile)  # Skip header line
                for line in txtfile:
                    parts = line.split()
                    date = parts[0]
                    amount = float(parts[1])
                    category = parts[2]
                    expense = Expense(date, amount, category)
                    self.expenses.append(expense)
            print("Expenses loaded successfully from", filename)
        except FileNotFoundError:
            print(f"File {filename} not found in directory {DIRECTORY}.")

def main():
    print("Welcome to ExpenseMaster!")
    expense_tracker = ExpenseTracker()

    # Load expenses from the CSV file
    expense_tracker.load_expenses_csv('expenses.csv')

    # Load expenses from the TXT file
    expense_tracker.load_expenses_txt('expense_data.txt')

    while True:
        print("\n1. Add Expense")
        print("2. Generate Report")
        print("3. Export Data")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            expense = Expense(date, amount, category)
            expense_tracker.add_expense(expense)
            print("Expense added successfully!")

        elif choice == "2":
            expense_tracker.generate_report()

        elif choice == "3":
            format = input("Enter export format (CSV or TXT): ")
            expense_tracker.export_data(format)

        elif choice == "4":
            print("Exiting ExpenseMaster. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()