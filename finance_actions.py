import csv
from datetime import datetime

def load_transactions(filename):
    """Load transactions from a CSV file into a list of dictionaries."""
    transactions = []
    
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            with open('errors.txt', 'a') as error_file:
                for row in reader:
                    try:
                        transactions.append(process_row(row))
                    except ValueError as e:
                        print(f"Error processing row {row}: {e}")
                        error_file.write(f"Error parsing row {row}: {e}\n")

    # For each row:
    #   Parse date with datetime.strptime
    #   Make amount negative for 'debit'
    #   Create dictionary with all fields
    #   Add to transactions
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        with open('errors.txt', 'a') as error_file:
            error_file.write(f"Error: The file {filename} was not found.\n")

    return transactions

def process_row(row):
    """Process a single row of data."""
    # Convert date to datetime object
    row['date'] = datetime.strptime(row['date'], '%Y-%m-%d')
    # Convert amount to float
    if row['type'] == 'debit':
        row['amount'] = -float(row['amount'])
    else:
        row['amount'] = float(row['amount'])
    # Convert transaction_id and customer_id to int
    row['transaction_id'] = int(row['transaction_id'])
    row['customer_id'] = int(row['customer_id'])
    return row