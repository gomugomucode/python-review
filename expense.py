from datetime import datetime


class Expense:
    """
    Represents a single expense record with amount, category, description, and date.
    """

    # In Python, constructors must be named '__init__' with TWO underscores on each side (dunder init).
    # Single underscore '_init_' is treated as a regular custom method and won't be called automatically!
    def __init__(self, amount, category, description="No description", date=None):
        self.amount = float(amount)
        self.category = category
        self.description = description
        # Automatically record current date and time if not explicitly provided
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        # __str__ defines how Python displays this object when printed (e.g. print(expense))
        return f"{self.date} | {self.category:<15} | ${self.amount:>8.2f} | {self.description}"
