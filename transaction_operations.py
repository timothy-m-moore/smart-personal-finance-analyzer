import user_interface
from datetime import datetime
from collections import Counter
import random

def add_transaction(transactions):
    """Add a new transaction from user input."""
    # Prompt for date, customer_id, amount, type, description
    # Validate date, amount, type
    # Generate new transaction_id
    # Create dictionary and append

    user_interface.add_ui_header("Adding Transaction")

    date = _get_date()
    cust_id = _get_customer_id(transactions)
    amount = _get_amount()
    transaction_type = _get_transaction_type()
    description = input("Enter description: ")
    transaction_id = max([t['transaction_id'] for t in transactions], default=0) + 1

    # Make debit amounts negative
    if transaction_type == 'debit':
        amount = -abs(amount)  # Ensure it's negative
    else:
        amount = abs(amount)   # Ensure credits/transfers are positive

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
            return abs(float(amount))
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
    user_interface.add_ui_header("Viewing Transactions")

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

    user_interface.display_transactions(transactions)

def _display_random_transactions(transactions):
    """Display 5 random transactions and return the sample for selection."""
    sample_size = min(5, len(transactions))
    random_transactions = random.sample(transactions, sample_size)

    print(f"Choose a transaction from these options:")
    print()

    # Display the random transactions in a simple table
    print(f"{'Option':<6} {'Transaction Id':<15} {'Customer':<8} {'Date':<12} {'Amount':<10} {'Type':<8}")
    print("-" * 70)

    for i, transaction in enumerate(random_transactions, 1):
        date_str = transaction['date'].strftime('%b %d, %Y')
        amount_str = f"${transaction['amount']:.2f}"
        
        print(f"{i:<6} {transaction['transaction_id']:<15} "
              f"{transaction['customer_id']:<8} {date_str:<12} "
              f"{amount_str:<10} {transaction['type']:<8}")

    return random_transactions

def _get_transaction_choice(random_transactions):
    """Get user's choice from the displayed random transactions."""
    sample_size = len(random_transactions)
    
    while True:
        try:
            choice = int(input(f"\nEnter your choice (1-{sample_size}): "))
            if 1 <= choice <= sample_size:
                return random_transactions[choice - 1]
            else:
                print(f"Please enter a number between 1 and {sample_size}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def update_transaction(transactions):
    """Update a transaction by transaction ID."""
    user_interface.add_ui_header("Updating Transaction")
    if not transactions:
        print("No transactions available to update.")
        return

    # Get 5 random transactions (or all if less than 5)
    sample_size = min(5, len(transactions))
    random_transactions = random.sample(transactions, sample_size)

    print("Choose a transaction to update from these options:")
    print()

    # Display random transactions and get user's choice
    random_transactions = _display_random_transactions(transactions)
    selected_transaction = _get_transaction_choice(random_transactions)

    # Get property to update
    property_name = _get_property_to_update()

    # Handle the update based on property type
    if property_name == "type":
        _update_transaction_type(selected_transaction)
    else:
        new_value = _get_new_property_value(property_name, transactions, selected_transaction)
        selected_transaction[property_name] = new_value
        print(f"\n{property_name.capitalize()} updated successfully!")

def _get_property_to_update():
    """Get the property name to update from user."""
    valid_properties = ['customer_id', 'date', 'amount', 'type', 'description']
    print(f"\nValid properties: {', '.join(valid_properties)}")
    
    while True:
        property_name = input("Enter the property name to update: ").strip().lower()
        if property_name in valid_properties:
            return property_name
        else:
            print(f"Invalid property. Choose from: {', '.join(valid_properties)}")

def _get_new_property_value(property_name, transactions, selected_transaction):
    """Get the new value for a property based on its type."""
    if property_name == "customer_id":
        return _get_customer_id(transactions)
    elif property_name == "date":
        return _get_date()
    elif property_name == "amount":
        amount = _get_amount()
        return _apply_amount_sign(amount, selected_transaction['type'])
    elif property_name == "description":
        return input("Enter new description: ")

def _update_transaction_type(selected_transaction):
    """Update transaction type and adjust amount sign accordingly."""
    new_type = _get_transaction_type()
    current_amount = abs(selected_transaction['amount'])
    
    selected_transaction['type'] = new_type
    selected_transaction['amount'] = _apply_amount_sign(current_amount, new_type)
    
    print(f"\nType and amount sign updated successfully!")

def _apply_amount_sign(amount, transaction_type):
    """Apply correct sign to amount based on transaction type."""
    return -abs(amount) if transaction_type == 'debit' else abs(amount)

def delete_transaction(transactions):
    """Delete a transaction by selecting from random options."""
    user_interface.add_ui_header("Deleting Transaction")
    if not transactions:
        print("No transactions available to delete.")
        return

    # Display random transactions and get user's choice
    random_transactions = _display_random_transactions(transactions)
    selected_transaction = _get_transaction_choice(random_transactions)

    # Show transaction details before deletion
    print(f"\nYou selected:")
    print(f"ID: {selected_transaction['transaction_id']}")
    print(f"Customer: {selected_transaction['customer_id']}")
    print(f"Date: {selected_transaction['date'].strftime('%b %d, %Y')}")
    print(f"Amount: ${selected_transaction['amount']:.2f}")
    print(f"Type: {selected_transaction['type']}")
    print(f"Description: {selected_transaction.get('description', '')}")

    # Confirm deletion
    confirm = input("\nAre you sure you want to delete this transaction? (y/n): ").strip().lower()
    if confirm in ['y', 'yes']:
        transactions.remove(selected_transaction)
        print("\nTransaction deleted successfully!")
    else:
        print("\nDeletion cancelled.")

def analyze_finances(transactions):
    """Calculate and display financial summaries."""
    user_interface.add_ui_header("Financial Analysis - 2022 Transactions")
    
    if not transactions:
        print("No transactions available for analysis.")
        return

    # Filter to only 2022 transactions
    transactions_2022 = [t for t in transactions if t['date'].year == 2022]
    
    if not transactions_2022:
        print("No transactions found for 2022.")
        return

    # Initialize totals
    totals_by_type = {'credit': 0.0, 'debit': 0.0, 'transfer': 0.0}
    customer_debits = {}
    
    # Sum amounts by type and track customer debits
    for transaction in transactions_2022:
        transaction_type = transaction['type'].lower()
        amount = abs(transaction['amount'])
        customer_id = transaction['customer_id']
        
        if transaction_type in totals_by_type:
            totals_by_type[transaction_type] += amount
        
        # Track customer debits
        if transaction_type == 'debit':
            if customer_id in customer_debits:
                customer_debits[customer_id] += amount
            else:
                customer_debits[customer_id] = amount

    # Calculate net balance (credits - debits, transfers don't affect balance)
    net_balance = totals_by_type['credit'] - totals_by_type['debit']
    
    # Calculate total amount for percentages
    total_amount = sum(totals_by_type.values())
    
    # Find customer with highest debit amount
    highest_debit_customer = None
    highest_debit_amount = 0
    if customer_debits:
        highest_debit_customer = max(customer_debits, key=customer_debits.get)
        highest_debit_amount = customer_debits[highest_debit_customer]

    # Prepare analysis text for both display and file
    analysis_lines = []
    analysis_lines.append("=== FINANCIAL ANALYSIS - 2022 TRANSACTIONS ===")
    analysis_lines.append("")
    analysis_lines.append("Financial Summary:")
    analysis_lines.append(f"Total Credits: ${totals_by_type['credit']:.2f}")
    analysis_lines.append(f"Total Debits: ${totals_by_type['debit']:.2f}")
    analysis_lines.append(f"Total Transfers: ${totals_by_type['transfer']:.2f}")
    analysis_lines.append(f"Net Balance: ${net_balance:.2f}")
    analysis_lines.append("")
    
    analysis_lines.append("By Type:")

    for transaction_type in ['credit', 'debit']:
        total = totals_by_type[transaction_type]
        if total > 0:
            analysis_lines.append(f"  {transaction_type.capitalize()}: ${total:.2f}")
    
    analysis_lines.append("")
    analysis_lines.append("Percentage by Type:")
    for transaction_type, total in totals_by_type.items():
        if total > 0 and total_amount > 0:
            percentage = (total / total_amount) * 100
            analysis_lines.append(f"  {transaction_type.capitalize()}: {percentage:.1f}%")
    
    analysis_lines.append("")
    if highest_debit_customer:
        analysis_lines.append("Customer with Highest Debit Amount:")
        analysis_lines.append(f"  Customer {highest_debit_customer}: ${highest_debit_amount:.2f}")
    else:
        analysis_lines.append("No debit transactions found.")

    # Display analysis
    for line in analysis_lines:
        print(line)

    # Save analysis to file
    try:
        with open('analysis.txt', 'w') as f:
            for line in analysis_lines:
                f.write(line + '\n')
        print(f"\nAnalysis saved to analysis.txt")
    except Exception as e:
        print(f"\nError saving analysis to file: {e}")

def generate_report(transactions, filename='report.txt'):
    """Generate a text report of financial summaries."""
    user_interface.add_ui_header("Generating Report")
    
    if not transactions:
        print("No transactions available for report generation.")
        return
    
    # Generate filename with current date
    current_date = datetime.now().strftime('%Y%m%d')
    base_name = filename.split('.')[0]  # Remove .txt extension if present
    dated_filename = f"{base_name}_{current_date}.txt"
    
    # Calculate metrics
    totals_by_type = {'credit': 0.0, 'debit': 0.0, 'transfer': 0.0}
    
    # Sum amounts by type
    for transaction in transactions:
        transaction_type = transaction['type'].lower()
        amount = abs(transaction['amount'])
        
        if transaction_type in totals_by_type:
            totals_by_type[transaction_type] += amount
    
    # Calculate net balance (credits - debits, transfers don't affect balance)
    net_balance = totals_by_type['credit'] - totals_by_type['debit']
    
    # Write to file
    try:
        with open(dated_filename, 'w') as f:
            f.write("Financial Summary\n")
            f.write(f"Total Credits: ${totals_by_type['credit']:.2f}\n")
            f.write(f"Total Debits: ${totals_by_type['debit']:.2f}\n")
            f.write(f"Total Transfers: ${totals_by_type['transfer']:.2f}\n")
            f.write(f"Net Balance: ${net_balance:.2f}\n")
            f.write("By Type:\n")
            
            for transaction_type in ['credit', 'debit']:
                total = totals_by_type[transaction_type]
                if total > 0:
                    f.write(f"  {transaction_type.capitalize()}: ${total:.2f}\n")
        
        print(f"Report successfully generated: {dated_filename}")
        
    except Exception as e:
        print(f"Error generating report: {e}")
        with open('errors.txt', 'a') as error_file:
            error_file.write(f"Error generating report {dated_filename}: {e}\n")