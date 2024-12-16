

def calculate_savings(total_income, total_expenses): #calculates the total savings.
    savings = total_income - total_expenses
    return 

def find_trends(sources):
    print(sources)
    if len(sources) >= 1:
        print("found, at least 1")
        highest_source_value = []
    if len(sources) >= 2:
        print("found, at least 2")
        second_highest_source_value = []
    if len(sources) >= 3:
        third_highest_source_value = []
        print("found, at least 3")
        
    if len(sources) >= 1:
        print(1)
        highest_value = 0
        highest_source = "null"
        for source in sources: #find the source with highest value
            if source[0] > highest_value:
                highest_value = source[0]
                highest_source = source[1]
        highest_source_value = [highest_value, highest_source]
        
        if len(sources) >= 2:
            print(2)
            highest_value = highest_source_value
            second_highest_value = 0
            second_highest_source = "null"
            for source in sources:
                if source[0] > second_highest_value and source[0] < highest_value:
                    second_highest_value = source[0]
                    second_highest_source = source[1]
            second_highest_source_value = [second_highest_value, second_highest_source]
            
            if len(sources) >= 3:
                print(3)
                third_highest_value = 0
                third_highest_source = "null"
                for source in sources:
                    if source[0] > third_highest_value and source[0] < second_highest_value:
                        third_highest_value = source[0]
                        third_highest_source = source[1]
                third_highest_source_value = [third_highest_value, third_highest_source]
    
    print (highest_source_value, second_highest_source_value, third_highest_source_value)
    
    if len(sources) <= 1:
        return highest_source_value
    elif len(sources) <= 2:
        return highest_source_value, second_highest_source_value
    elif len(sources) <= 3:
        return highest_source_value, second_highest_source_value, third_highest_source_value
                        
        
            
    
def generate_report(total_income, total_expenses, savings, budget, income_entries, expense_entries): #generates a report.
    income_source_array = [] #array to store the sources of income and how much has been spent.
    
    for entry in income_entries: #this loop checks if the source of the entry is already in source_array.
        already_added = False
        for item in income_source_array:
            if entry[1] == item[1]:
                already_added = True #if it's in the array, add the amount spent onto what was already there and break the loop.
                item[0] += entry[0]
            if already_added == True:
                break
        if already_added == False:
            income_source_array.append(entry)
    print(income_source_array)
    
    print(find_trends(income_source_array))
    
    
    
    
    if budget >= total_expenses: #check if you went over your budget; the text will change if you did.
        #return(f"You made £{total_income} and spent £{total_expenses} out of your budget of £{budget}. Overall you saved £{savings}.")
        return(f"")
    else:
        return(f"You made £{total_income} and spent £{total_expenses}. You spent £{total_expenses-budget} more than your budget of £{budget}.")


generate_report(1000,700, calculate_savings(1000, 700), 900, [[200, "source1"],[300,"source2"],[600,"source1"],[10,"source2"], [50, "source3"]], "expenses")