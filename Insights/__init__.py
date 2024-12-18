

def calculate_savings(total_income, total_expenses): #calculates the total savings.
    savings = total_income - total_expenses
    return savings

def find_highest(sources):
    highest = 0
    highest_source = None
    for source, value in sources.items():
        if value > highest:
            highest = value
            highest_source = source
    return highest, highest_source
    
def generate_report(total_income, total_expenses, over_budget, over_budget_difference, income_entries, expense_entries): #generates a report.
    
    highest_expense, highest_expense_source = find_highest(expense_entries)
    highest_income, highest_income_source = find_highest(income_entries)
    savings = calculate_savings(total_income, total_expenses)
    
    if over_budget == True: #check if you went over your budget; the text will change if you did
        #return(f"You made £{total_income} and spent £{total_expenses} out of your budget of £{budget}. Overall you saved £{savings}.")
        return(f"You made £{total_income} in total. Your highest source of income was {highest_income_source} which made you £{highest_income}. Overall you spent £{total_expenses} with the source you spend the most money on being {highest_expense_source}, which you spent £{highest_expense} on. You saved £{savings} in total. You went over your budget by £{over_budget_difference}.")
    else:
        return(f"You made £{total_income} in total. Your highest source of income was {highest_income_source} which made you £{highest_income}. Overall you spent £{total_expenses} with the source you spend the most money on being {highest_expense_source}, which you spent £{highest_expense} on. You saved £{savings} in total.")

"""
expenselist = {
    "source1": 200,
    "source2": 300,
    "source3": 10,
    "source4": 413,
    "source5": 43
}

incomelist = {
    "source1": 200,
    "source2": 300,
    "source3": 10,
    "source4": 413,
    "source5": 43
}

print(generate_report(1000,700, True, 50, expenselist, incomelist))"""