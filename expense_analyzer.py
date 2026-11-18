# Pure Python Expense & Budget Analyzer

expenses = [
    {"item": "Groceries", "category": "Food", "amount": 1850},
    {"item": "Cab & Commute", "category": "Transport", "amount": 950},
    {"item": "Protein & Oats", "category": "Fitness", "amount": 2200},
    {"item": "Dinner Outing", "category": "Food", "amount": 650},
    {"item": "Internet & Mobile", "category": "Utilities", "amount": 799},
]

MONTHLY_BUDGET = 8000

def analyze_expenses(records, budget):
    total_spent = 0
    category_totals = {}

    for entry in records:
        amount = entry["amount"]
        category = entry["category"]
        total_spent += amount
        category_totals[category] = category_totals.get(category, 0) + amount

    remaining = budget - total_spent
    highest_category = max(category_totals, key=category_totals.get)

    print("====== MONTHLY EXPENSE REPORT ======")
    print(f"Total Budget     : Rs. {budget}")
    print(f"Total Spent      : Rs. {total_spent}")
    print(f"Remaining Budget : Rs. {remaining}")
    print(f"Top Spend Area   : {highest_category} (Rs. {category_totals[highest_category]})")
    print("\n--- Category Breakdown ---")
    for cat, amt in category_totals.items():
        print(f"- {cat:<12}: Rs. {amt}")

if __name__ == "__main__":
    analyze_expenses(expenses, MONTHLY_BUDGET)
    