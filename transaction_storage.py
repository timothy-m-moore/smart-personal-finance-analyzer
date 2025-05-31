import csv
import datetime

def load_transactions(filename = 'financial_transactions.csv'):
    """Load transactions from a CSV file into a list of dictionaries."""
    transactions = []
    print('Loading transactions...')
    
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            with open('errors.txt', 'a') as error_file:
                for row in reader:
                    try:
                        transactions.append(_process_row(row))
                    except ValueError as e:
                        print(f"Error processing row {row}: {e}")
                        error_file.write(f"Error parsing row {row}: {e}\n")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        with open('errors.txt', 'a') as error_file:
            error_file.write(f"Error: The file {filename} was not found.\n")

    print(f"Loaded {len(transactions)} transactions from {filename}.")
    return transactions

def _process_row(row):
    row['date'] = _convert_date(row['date'])
    row['amount'] = _convert_amount(row['amount'], row['type'])
    row['transaction_id'] = _convert_to_int(row['transaction_id'])
    row['customer_id'] = _convert_to_int(row['customer_id'])
    return row

def _convert_date(date_string):
    return datetime.datetime.strptime(date_string, '%Y-%m-%d')

def _convert_amount(amount_string, transaction_type):
    amount = float(amount_string)
    return -amount if transaction_type == 'debit' else amount

def _convert_to_int(value_string):
    return int(value_string)