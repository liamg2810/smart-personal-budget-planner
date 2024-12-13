

def calculate_savings(total_income, total_expenses):
    savings = total_income - total_expenses
    return savings
    

def generate_report(total_income, total_expenses, savings, budget):
    if budget >= total_expenses:
        print(f"You made £{total_income} and spent £{total_expenses} out of your budget of £{budget}. Overall you saved £{savings}.")
    else:
        print(f"You made £{total_income} and spent £{total_expenses}. You spent £{total_expenses-budget} more than your budget of £{budget}.")
