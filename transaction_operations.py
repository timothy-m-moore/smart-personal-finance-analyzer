from user_interface import add_ui_header
from datetime import datetime
from collections import Counter

def add_transaction(transactions):
    """Add a new transaction from user input."""
    # Prompt for date, customer_id, amount, type, description
    # Validate date, amount, type
    # Generate new transaction_id
    # Create dictionary and append

    add_ui_header("Adding Transaction")

    date = _get_date()
    cust_id = _get_customer_id(transactions)
    amount = _get_amount()
    transaction_type = _get_transaction_type()
    description = input("Enter description: ")
    transaction_id = max([t['transaction_id'] for t in transactions], default=0) + 1
    transaction = {
        'transaction_id': transaction_id,
        'date': date,
        'customer_id': cust_id,
        'amount': amount,
        'type': transaction_type,
        'description': description
    }

    transactions.append(transaction)
    print(f"Transaction added!")

def _get_date():
    """Get date from user input."""
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            return datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def _get_customer_id(transactions):
    """Get customer ID from user input."""
    if transactions:
        _display_top_customer_ids(transactions)

    while True:
        cust_id = input("Enter customer ID: ")
        if cust_id.isdigit():
            return int(cust_id)
        else:
            print("Invalid customer ID. Please enter a number.")

def _display_top_customer_ids(transactions):
    customer_counts = Counter(t['customer_id'] for t in transactions)
    top_5 = customer_counts.most_common(5)
        
    if top_5:
        print("Most frequent customer IDs:")
        for customer_id, count in top_5:
            print(f"  {customer_id} (appears {count} times)")

def _get_amount():
    """Get amount from user input."""
    while True:
        amount = input("Enter amount: ")
        try:
            return float(amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")

def _get_transaction_type():
    """Get transaction type from user input."""
    while True:
        type = input("Enter transaction type (credit/debit/transfer): ").strip().lower()
        if type in ['credit', 'debit', 'transfer']:
            return type
        else:
            print("Invalid transaction type. Please enter 'credit', 'debit', or 'transfer'.")

def view_transactions(transactions):
    """Display the transactions."""
    add_ui_header("Viewing Transactions")

    if not transactions:
        print("No transactions available.")
        return

    transaction_type = input("Enter transaction type to filter (credit/debit/transfer) or press Enter to view all: ").strip().lower()
    if transaction_type and transaction_type not in ['credit', 'debit', 'transfer']:
        print("Invalid transaction type. Showing all transactions.")
        transaction_type = None

    # Filter transactions by type if specified
    if transaction_type:
        transactions = [t for t in transactions if t['type'] == transaction_type]

    # Print header
    print(f"{'ID':<4} | {'Customer':<8} | {'Date':<12} | {'Amount':<10} | {'Type':<8} | {'Description':<20}")
    print("-" * 70)

    # Print each transaction
    for transaction in transactions:
        date_str = transaction['date'].strftime('%b %d, %Y')
        amount_str = f"${transaction['amount']:.2f}"
        
        print(f"{transaction['transaction_id']:<4} | "
              f"{transaction['customer_id']:<8} | "
              f"{date_str:<12} | "
              f"{amount_str:<10} | "
              f"{transaction['type']:<8} | "
              f"{transaction.get('description', ''):<20}")