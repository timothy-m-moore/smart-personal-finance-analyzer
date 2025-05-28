import transaction_storage
import user_interface
import transaction_operations

transaction_file_name = 'financial_transactions.csv'
transactions = transaction_storage.load_transactions(transaction_file_name)

try:
    while True:
        user_interface.display_menu()
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            transaction_operations.add_transaction(transactions)
        elif choice == '2':
            transaction_operations.view_transactions(transactions)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
except KeyboardInterrupt:
    print("\nExiting the program.")