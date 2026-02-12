class Category:
    """
    Represents a budget category (e.g., Food, Clothing).
    Supports deposits, withdrawals, transfers, and balance tracking.
    """

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""

        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

    def deposit(self, amount, description=""):
        if amount <= 0:
            return False
        self.ledger.append({"amount": amount, "description": description})
        return True

    def withdraw(self, amount, description=""):
        if amount <= 0:
            return False

        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount


def create_spend_chart(categories):
    """
    Creates a bar chart showing percentage spent by category.
    """

    title = "Percentage spent by category\n"
    withdrawals = []
    total_spent = 0

    # Calculate total withdrawals
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        withdrawals.append(spent)
        total_spent += spent

    # Calculate percentage rounded down to nearest 10
    percentages = []
    for spent in withdrawals:
        percent = int((spent / total_spent) * 100) if total_spent > 0 else 0
        percent -= percent % 10
        percentages.append(percent)

    # Build chart
    chart = title

    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percent in percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(category.name) for category in categories)

    for i in range(max_len):
        chart += "     "
        for category in categories:
            chart += category.name[i] + "  " if i < len(category.name) else "   "
        chart += "\n"

    return chart.rstrip("\n")
