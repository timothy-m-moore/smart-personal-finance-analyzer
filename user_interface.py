from menu_options import MenuOption

def display_menu():
    """Display the main menu options."""
    MenuOption.display_menu()

def get_user_choice():
    """Get and validate user menu choice."""
    while True:
        choice = input("\nEnter your choice: ").strip()
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue
        option = MenuOption.get_by_number(choice)
        if option:
            return option
        else:
            print("Invalid choice. Please try again.")

def run_application():
    """Run the main application loop."""
    transactions = []
    
    try:
        while True:
            display_menu()
            option = get_user_choice()
            
            if option == MenuOption.EXIT:
                print("Exiting the program. Goodbye!")
                break
            elif option == MenuOption.LOAD_TRANSACTIONS:
                file_to_load = input("Enter the filename to load transactions from (leave blank for 'financial_transactions.csv'): ").strip()
                if not file_to_load:
                    transactions = option.function()
                else:
                    transactions = option.function(file_to_load)
            elif option.function:
                option.function(transactions)
            else:
                print(f"Function not implemented for {option.description}")
                
    except KeyboardInterrupt:
        print("\nExiting the program.")

def add_ui_header(function_name):
    """Display a header for the given function of the UI."""
    asterisk_length = len(function_name) + 4
    print("\n")
    print("*" * asterisk_length)
    print(f"* {function_name} *")
    print("*" * asterisk_length)
    print("\n")

def display_transactions(transactions):
    """Display the transactions in a formatted way."""
    if not transactions:
        print("No transactions available.")
        return
    
    # Print header
    print("\n" + "=" * 70)
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