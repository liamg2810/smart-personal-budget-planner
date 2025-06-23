

def calculate_savings(total_income, total_expenses):
    return total_income - total_expenses

def find_highest(sources):
    highest = 0
    highest_source = None
    for source, value in sources.items():
        if value > highest:
            highest = value
            highest_source = source
    return highest, highest_source
    
def generate_report(total_income, total_expenses, over_budget, over_budget_difference, income_entries, expense_entries):
    
    #Error Raising
    if type(total_income) != int:
        raise TypeError("Total income is not an integer.")
    if type(total_expenses) != int:
        raise TypeError("Total expenses is not an integer.")
    if type(over_budget) != bool:
        raise TypeError("Over budget is not a boolean.")
    if type(over_budget_difference) != int:
        raise TypeError("Over budget difference is not an integer.")
    
    highest_expense, highest_expense_source = find_highest(expense_entries)
    highest_income, highest_income_source = find_highest(income_entries)
    savings = calculate_savings(total_income, total_expenses)
    
    #Report Generation
    if over_budget == True:
        if savings > 0:
            return(f"You made £{total_income} in total.\nYour highest source of income was {highest_income_source} which made you £{highest_income}.\nOverall you spent £{total_expenses} with the source you spend the most money on being {highest_expense_source}, which you spent £{highest_expense} on.\nYou saved £{savings} in total.\nYou went over your budget by £{over_budget_difference}.")
        else:
            return(f"You made £{total_income} in total.\nYour highest source of income was {highest_income_source} which made you £{highest_income}.\nOverall you spent £{total_expenses} with the source you spend the most money on being {highest_expense_source}, which you spent £{highest_expense} on.\nYou went over your budget by £{over_budget_difference}.")
    else:
        if savings > 0:
            return(f"You made £{total_income} in total.\nYour highest source of income was {highest_income_source} which made you £{highest_income}.\nOverall you spent £{total_expenses} with the source you spend the most money on being {highest_expense_source}, which you spent £{highest_expense} on.\nYou saved £{savings} in total.")
        else:
            return(f"You made £{total_income} in total.\nYour highest source of income was {highest_income_source} which made you £{highest_income}.\nOverall you spent £{total_expenses} with the source you spend the most money on being {highest_expense_source}, which you spent £{highest_expense} on.")
