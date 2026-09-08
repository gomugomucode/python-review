from InquirerPy import inquirer
from viewexpense import ViewExpense


def main():
    """
    Main application flow for the Expense Tracker CLI.
    """
    # Create an instance of ViewExpense.
    # Because ViewExpense inherits from AddExpense, this single 'tracker' object:
    # 1. Holds the 'self.expenses' list
    # 2. Can add expenses via 'tracker.prompt_add_expense()'
    # 3. Can view expenses via 'tracker.view_expenses()'
    # 4. Can update expenses via 'tracker.prompt_update_expense()'
    # 5. Can delete expenses via 'tracker.prompt_delete_expense()'
    tracker = ViewExpense()

    print("========================================")
    print("       Expense Tracker CLI              ")
    print("========================================")

    # 1. Use inquirer.confirm to ask the user a Yes/No question interactively
    # default=True sets 'Yes' as the default choice (press Enter to accept)
    start = inquirer.confirm(
        message="Do you want to manage your expense data?",
        default=True,
    ).execute()

    if not start:
        print("\nThank you for using the expense tracker. Have a great day!\n")
        return

    # 2. Main menu loop: keeps prompting the user until they choose to Exit
    while True:
        # inquirer.select presents an interactive menu with arrow key navigation
        # 'name' is what the user sees on screen, 'value' is what gets returned to the code
        action = inquirer.select(
            message="Main Menu - What would you like to do?",
            choices=[
                {"name": "1. Add Expense", "value": "add"},
                {"name": "2. View Expenses", "value": "view"},
                {"name": "3. Update Expense", "value": "update"},
                {"name": "4. Delete Expense", "value": "delete"},
                {"name": "5. Exit", "value": "exit"},
            ],
            default="add",
        ).execute()

        # Execute corresponding action based on the selected choice
        if action == "add":
            tracker.prompt_add_expense()
        elif action == "view":
            tracker.view_expenses()
        elif action == "update":
            tracker.prompt_update_expense()
        elif action == "delete":
            tracker.prompt_delete_expense()
        elif action == "exit":
            # Ask for confirmation before exiting
            confirm_exit = inquirer.confirm(
                message="Are you sure you want to exit?",
                default=True,
            ).execute()
            if confirm_exit:
                print("\nThank you for using the expense tracker. Goodbye!\n")
                break


# In Python, '__name__ == "__main__"' ensures this code only runs when executing this file directly,
# not when imported by another file.
if __name__ == "__main__":
    main()
