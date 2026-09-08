from InquirerPy import inquirer
from addexpense import AddExpense
import json
import os

filename = "expense.json"


class ViewExpense(AddExpense):
    """
    Inherits from AddExpense. This allows ViewExpense to access 'self.expenses'
    and all methods from AddExpense, while adding viewing, updating, and deleting.
    """

    def view_expenses(self):
        """
        Prints all expenses in a clean formatted table with a total summary.
        """
        print("\n--- All Expenses ---")

        # Check if any expenses exist
        if not self.expenses:
            print("No expenses recorded yet. Use 'Add Expense' to record one!\n")
            return

        # Print header
        header = f"{'#':<4} {'Date & Time':<18} {'Category':<20} {'Amount':>10}   {'Description'}"
        print(header)
        print("-" * len(header) + "-" * 15)

        total_amount = 0.0
        # Enumerate through self.expenses to show 1-based index
        for idx, exp in enumerate(self.expenses, start=1):
            total_amount += exp.amount
            print(
                f"{idx:<4} {exp.date:<18} {exp.category:<20} ${exp.amount:>9.2f}   {exp.description}"
            )

        print("-" * len(header) + "-" * 15)
        print(
            f"Total Entries: {len(self.expenses)} | Total Spent: ${total_amount:.2f}\n"
        )

    def prompt_update_expense(self):
        """
        Uses InquirerPy to let the user select an expense and choose which field to modify.
        """
        print("\n--- Update Expense ---")

        if not self.expenses:
            print("No expenses to update. Add an expense first!\n")
            return

        # Build list of options for inquirer.select
        # Each choice has a 'name' (displayed text) and a 'value' (index in self.expenses)
        choices = [
            {
                "name": f"#{i + 1} | {exp.category} | ${exp.amount:.2f} | {exp.description}",
                "value": i,
            }
            for i, exp in enumerate(self.expenses)
        ]
        choices.append({"name": "Cancel", "value": None})

        selected_idx = inquirer.select(
            message="Select the expense to update:",
            choices=choices,
        ).execute()

        # If user selected Cancel
        if selected_idx is None:
            print("Update cancelled.\n")
            return

        target = self.expenses[selected_idx]
        print(
            f"\nEditing: #{selected_idx + 1} ({target.category} - ${target.amount:.2f})"
        )

        # Let user choose what attribute to update
        field = inquirer.select(
            message="What would you like to update?",
            choices=["Amount", "Category", "Description", "All Details", "Cancel"],
        ).execute()

        if field == "Cancel":
            print("Update cancelled.\n")
            return

        # Update Amount if selected
        if field in ("Amount", "All Details"):
            new_amount = inquirer.number(
                message=f"Enter new amount (current: {target.amount}):",
                float_allowed=True,
                min_allowed=0.01,
                default=float(target.amount),
            ).execute()
            target.amount = float(new_amount)

        # Update Category if selected
        if field in ("Category", "All Details"):
            new_category = inquirer.select(
                message="Select new category:",
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
                default=target.category,
            ).execute()
            if new_category == "Other":
                new_category = inquirer.text(
                    message="Enter custom category name:",
                    default=target.category,
                ).execute()
            target.category = new_category

        # Update Description if selected
        if field in ("Description", "All Details"):
            new_description = inquirer.text(
                message="Enter new description:",
                default=target.description,
            ).execute()
            target.description = new_description

        print("\n[OK] Expense updated successfully!\n")

        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump([], f)

    def prompt_delete_expense(self):
        """
        Uses InquirerPy to let the user pick an expense to delete, with confirmation prompt.
        """
        print("\n--- Delete Expense ---")

        if not self.expenses:
            print("No expenses to delete. Add an expense first!\n")
            return

        choices = [
            {
                "name": f"#{i + 1} | {exp.category} | ${exp.amount:.2f} | {exp.description}",
                "value": i,
            }
            for i, exp in enumerate(self.expenses)
        ]
        choices.append({"name": "Cancel", "value": None})

        selected_idx = inquirer.select(
            message="Select the expense to delete:",
            choices=choices,
        ).execute()

        if selected_idx is None:
            print("Deletion cancelled.\n")
            return

        target = self.expenses[selected_idx]

        # Use inquirer.confirm to ask for user confirmation before permanently deleting
        confirmed = inquirer.confirm(
            message=f"Are you sure you want to delete #{selected_idx + 1} ({target.category} - ${target.amount:.2f})?",
            default=False,
        ).execute()

        if confirmed:
            removed = self.expenses.pop(selected_idx)
            print(
                f"\n[OK] Successfully deleted: {removed.category} (${removed.amount:.2f})\n"
            )
        else:
            print("Deletion cancelled.\n")
