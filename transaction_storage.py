import csv
import datetime
from csv_headers import TransactionHeaders

def load_transactions(filename = 'financial_transactions.csv'):
    """Load transactions from a CSV file into a list of dictionaries."""
    transactions = []
    print('Loading transactions...')
    
    try:
        with open(filename, newline='') as csvfile:
            # Check if file has headers
            sample = csvfile.read(1024)
            csvfile.seek(0)
            
            # Try to detect if first row contains headers
            sniffer = csv.Sniffer()
            has_header = sniffer.has_header(sample)
            
            if has_header:
                reader = csv.DictReader(csvfile)
                # Validate headers
                headers = reader.fieldnames
                is_valid, missing = TransactionHeaders.validate_headers(headers)
                if not is_valid:
                    print(f"Missing headers detected: {missing}. Using default headers...")
                    # Reset file position and create new reader with default headers
                    csvfile.seek(0)
                    next(csvfile)  # Skip the invalid header row
                    reader = csv.DictReader(csvfile, fieldnames=TransactionHeaders.get_all_headers())
            else:
                # No headers detected, use our default headers
                print("No headers detected. Using default headers...")
                reader = csv.DictReader(csvfile, fieldnames=TransactionHeaders.get_all_headers())
            
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

def save_transactions(transactions, filename='financial_transactions.csv'):
    """Save transactions to a CSV file."""
    if not transactions:
        print("No transactions to save.")
        return
    
    try:
        with open(filename, 'w', newline='') as csvfile:
            # Get headers from the TransactionHeaders class
            headers = TransactionHeaders.get_all_headers()
            
            # Create CSV writer with headers
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            
            # Write header row
            writer.writeheader()
            
            # Write each transaction
            for transaction in transactions:
                # Convert datetime back to string for CSV
                row = transaction.copy()  # Don't modify original
                row['date'] = transaction['date'].strftime('%Y-%m-%d')
                
                # Ensure amount is positive for CSV (type indicates debit/credit)
                row['amount'] = f"{abs(transaction['amount']):.2f}"
                
                writer.writerow(row)
        
        print(f"Successfully saved {len(transactions)} transactions to {filename}")
        
    except Exception as e:
        print(f"Error saving transactions to {filename}: {e}")
        with open('errors.txt', 'a') as error_file:
            error_file.write(f"Error saving transactions to {filename}: {e}\n")