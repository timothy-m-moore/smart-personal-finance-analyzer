import csv
from datetime import datetime

transaction_file_name = 'financial_transactions.csv'

def load_transactions(filename):
    """Load transactions from a CSV file into a list of dictionaries."""
    transactions = []
    # Open file with 'with' statement
    # Use csv.DictReader
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transactions.append(row)

    # For each row:
    #   Parse date with datetime.strptime
    #   Make amount negative for 'debit'
    #   Create dictionary with all fields
    #   Add to transactions
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")

    return transactions

load_transactions(transaction_file_name)