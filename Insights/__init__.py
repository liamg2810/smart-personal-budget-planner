

def calculate_savings(total_income, total_expenses): #calculates the total savings.
    savings = total_income - total_expenses
    return savings

def find_highest(sources):
    highest = None
    highest_source = None
    for source, value in sources.items():
        if value > highest:
            highest = value
            highest_source = source
    return highest, highest_source
    
def generate_report(total_income, total_expenses, budget, income_entries, expense_entries): #generates a report.
    
    highest_expense, highest_expense_source = find_highest(expense_entries)
    savings = calculate_savings(total_income, total_expenses)
    
    if budget >= total_expenses: #check if you went over your budget; the text will change if you did.
        #return(f"You made £{total_income} and spent £{total_expenses} out of your budget of £{budget}. Overall you saved £{savings}.")
        return(f"")
    else:
        return(f"You made £{total_income} and spent £{total_expenses}. You spent £{total_expenses-budget} more than your budget of £{budget}.")
"""
expenselist = {
    "source1": 200,
    "source2": 300,
    "source3": 10,
    "source4": 413,
    "source5": 43
}
"""


#generate_report(1000,700, 900, "income", expenselist)