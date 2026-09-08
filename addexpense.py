from InquirerPy import inquirer
from expense import Expense
import json
import os

filename = "expense.json"


class AddExpense:
    """
    Manages the expense collection and provides methods to add new expenses.
    Notice: AddExpense does NOT need to inherit from Expense because an 'expense manager'
    HAS expenses (composition), rather than BEING an expense itself (inheritance).
    """

    def __init__(self):
        # self.expenses holds the list of all Expense instances
        self.expenses = []

    def add_expense(self, amount, category, description="No description"):
        """
        Creates a new Expense object and adds it to the internal expenses list.
        """
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        print("\n[OK] Expense added successfully!\n")
        return expense

    def save_expenses(self):
        with open(filename, "w") as f:
            json.dump(self.expenses, f, indent=4)

    def load_expenses(self):
        if not os.path.exists(filename):
            return
        with open(filename, "r") as f:
            self.expenses = json.load(f)

    def prompt_add_expense(self):
        """
        Uses InquirerPy interactive prompts to gather expense details from the terminal:
        1. inquirer.number -> validates amount input as a positive number
        2. inquirer.select -> arrow-key category selection
        3. inquirer.text   -> optional description text
        """
        print("\n--- Add New Expense ---")

        # 1. Prompt for Amount using inquirer.number
        # float_allowed=True lets users enter decimals (e.g., 25.50)
        # min_allowed=0.01 prevents zero or negative amounts
        amount = inquirer.number(
            message="Enter amount ($):",
            float_allowed=True,
            min_allowed=0.01,
            invalid_message="Please enter a valid positive amount (> 0)",
        ).execute()

        # 2. Prompt for Category using inquirer.select with arrow-key navigation
        category = inquirer.select(
            message="Choose a category:",
            choices=[
                "Food & Dining",
                "Groceries",
                "Transportation",
                "Bills & Utilities",
                "Shopping",
                "Entertainment",
                "Health & Fitness",
                "Other",
            ],
            default="Food & Dining",
        ).execute()

        # If user picked 'Other', let them type their own custom category name
        if category == "Other":
            category = inquirer.text(
                message="Enter custom category name:",
                default="Other",
            ).execute()

        # 3. Prompt for Description using inquirer.text
        description = inquirer.text(
            message="Enter description (optional):",
            default="No description",
        ).execute()

        # Save the expense into self.expenses
        return self.add_expense(float(amount), category, description)
