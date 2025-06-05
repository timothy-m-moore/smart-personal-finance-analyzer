from enum import Enum
import transaction_storage
import transaction_operations

class MenuOption(Enum):
    LOAD_TRANSACTIONS = (1, "Load transactions from file", transaction_storage.load_transactions)
    ADD_TRANSACTION = (2, "Add a new transaction", transaction_operations.add_transaction)
    VIEW_TRANSACTIONS = (3, "View transactions", transaction_operations.view_transactions)
    UPDATE_TRANSACTION = (4, "Update a transaction", transaction_operations.update_transaction)
    DELETE_TRANSACTION = (5, "Delete a transaction", transaction_operations.delete_transaction)
    ANALYZE_FINANCES = (6, "Analyze finances", transaction_operations.analyze_finances)
    SAVE_TRANSACTIONS = (7, "Save transactions to file", transaction_storage.save_transactions)
    GENERATE_REPORT = (8, "Generate a report", transaction_operations.generate_report)
    EXIT = (9, "Exit the program", None)

    def __init__(self, number, description, function):
        self.number = number
        self.description = description
        self.function = function
        
    @classmethod
    def get_by_number(cls, number):
        '''Get menu option by number.'''
        for option in cls:
            if option.number == int(number):
                return option
        return None
    
    @classmethod
    def display_menu(cls):
        """Display all menu options."""
        print("\n" + "="*50)
        print("PERSONAL FINANCE ANALYZER")
        print("="*50)
        for option in cls:
            print(f"{option.number}. {option.description}")
        print("="*50)