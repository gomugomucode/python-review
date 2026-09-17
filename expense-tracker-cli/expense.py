from datetime import datetime


class Expense:
    """
    Represents a single expense record with amount, category, description, and date.
    """

    def __init__(self, amount, category, description="No description", date=None):
        self.amount = float(amount)
        self.category = category
        self.description = description
        # Automatically record current date and time if not explicitly provided
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        """
        Converts the Expense object into a standard Python dictionary.
        This is necessary because Python's json.dump() cannot save custom objects directly;
        it only knows how to save basic types like dictionaries, lists, strings, and numbers.
        """
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Reconstructs an Expense object from a dictionary loaded from JSON.
        This ensures self.expenses contains real Expense objects, not plain dictionaries.
        """
        return cls(
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            date=data["date"],
        )

    def __str__(self):
        # __str__ defines how Python displays this object when printed (e.g. print(expense))
        return f"{self.date} | {self.category:<15} | ${self.amount:>8.2f} | {self.description}"
