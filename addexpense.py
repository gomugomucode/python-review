from InquirerPy import inquirer
from expense import Expense
import json
import os

filename = "expense.json"


class AddExpense:
    """
    Manages the expense collection and provides methods to add, save, and load expenses.
    """

    def __init__(self):
        # self.expenses holds the list of all Expense instances
        self.expenses = []
        # Automatically load any previously saved expenses from expense.json when the app starts
        self.load_expenses()

    def save_expenses(self):
        """
        Saves all expenses to expense.json.
        We convert each Expense object to a dictionary using exp.to_dict() before saving.
        """
        data = [exp.to_dict() for exp in self.expenses]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_expenses(self):
        """
        Loads saved expenses from expense.json.
        We convert each dictionary back into an Expense object using Expense.from_dict().
        """
        if not os.path.exists(filename):
            return

        try:
            with open(filename, "r") as f:
                data = json.load(f)
                # Re-create Expense instances for each saved item
                self.expenses = [Expense.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError):
            # If the file is empty or corrupted, start with an empty list
            self.expenses = []

    def add_expense(self, amount, category, description="No description"):
        """
        Creates a new Expense object, adds it to the list, and saves to JSON.
        """
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        # Save to JSON immediately so data persists even if the app is closed
        self.save_expenses()
        print("\n[OK] Expense added and saved successfully!\n")
        return expense

    def prompt_add_expense(self):
        """
        Uses InquirerPy interactive prompts to gather expense details from the terminal:
        1. inquirer.number -> validates amount input as a positive number
        2. inquirer.select -> arrow-key category selection
        3. inquirer.text   -> optional description text
        """
        print("\n--- Add New Expense ---")

        # 1. Prompt for Amount using inquirer.number
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

        # Save the expense into self.expenses and persist to JSON
        return self.add_expense(float(amount), category, description)
