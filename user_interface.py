def display_menu():
    """Display the main menu of the user interface."""

    add_ui_header("Main Menu")
    print("1. Add transaction")
    print("2. View transactions")
    print("3. Exit")

def add_ui_header(function_name):
    """Display a header for the given function of the UI."""
    asterisk_length = len(function_name) + 4
    print("\n")
    print("*" * asterisk_length)
    print(f"* {function_name} *")
    print("*" * asterisk_length)
    print("\n")