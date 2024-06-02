from flask import Flask, request, render_template, send_file
import csv
import os

app = Flask(__name__)

DIRECTORY = r'/home/JosephJimenez07/mysite'

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

    def export_to_csv(self):
        csv_file_path = os.path.join(DIRECTORY, 'expenses.csv')
        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = ['Date', 'Amount', 'Category']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for expense in self.expenses:
                writer.writerow({'Date': expense.date, 'Amount': expense.amount, 'Category': expense.category})
        return csv_file_path

    def export_to_txt(self):
        txt_file_path = os.path.join(DIRECTORY, 'expense_data.txt')
        with open(txt_file_path, 'w') as txtfile:
            txtfile.write("Date       Amount   Category\n")
            for expense in self.expenses:
                txtfile.write(f"{expense.date} {expense.amount:>8}   {expense.category}\n")
        return txt_file_path

expense_tracker = ExpenseTracker()

@app.route('/add_expense', methods=['POST'])
def add_expense():
    date = request.form['date']
    amount = float(request.form['amount'])
    category = request.form['category']
    print(f"Adding expense: {date}, {amount}, {category}")  # Debugging output
    expense = Expense(date, amount, category)
    expense_tracker.add_expense(expense)
    return "Expense added successfully!"

@app.route('/export', methods=['POST'])
def export_data():
    format = request.form['format']
    print(f"Exporting data in format: {format}")  # Debugging output
    if format == 'csv':
        file_path = expense_tracker.export_to_csv()
    elif format == 'txt':
        file_path = expense_tracker.export_to_txt()
    else:
        return "Unsupported format", 400
    print(f"File path: {file_path}")  # Debugging output
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)