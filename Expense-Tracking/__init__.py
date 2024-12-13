expenses = ()


def add_expense(category, amount):
    try:
        amount = float(amount)  
        expenses.append({"category": category, "amount": amount})
        print(f"Expense added: {category} - {amount}")
    except ValueError:
        print("Invalid amount, enter a numeric value.")


def get_total_expenses():
    total_amount = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: {total_amount}")
    return total_amount


def get_expenses_by_category(category):
    category_expenses = [expense for expense in expenses if expense["category"] == category]
    if category_expenses:
        print(f"Expenses for category '{category}':")
        for expense in category_expenses:
            print(f"- {expense['amount']}")
    else:
        print(f"No expenses found for category '{category}'.")

def main():
    while True:
        print("\nExpense Tracker Menu:\n")
        print("1. Add an Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by Category")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter the expense category: ")
            amount = input("Enter the expense amount: ")
            add_expense(category, amount)
        elif choice == "2":
            get_total_expenses()
        elif choice == "3":
            category = input("Enter the category to view expenses: ")
            get_expenses_by_category(category)
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

