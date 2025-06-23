import subprocess
try:
    import json, time, os
    from colorama import Fore, Back, Style, init
except:
    print("Updating the required modules: \njson, time, os, colorama\n")
    try:
        subprocess.run(["python", "-m", "pip", "install", "json"])
        subprocess.run(["python", "-m", "pip", "install", "time"])
        subprocess.run(["python", "-m", "pip", "install", "os"])
        subprocess.run(["python", "-m", "pip", "install", "colorama"])
        print("Modules updated successfully\n")
        os._exit(0)
    except:
        print("Failed to update the required modules\n")
        os._exit(0)
init(autoreset=True)
budgetdata = {}
def main():
    while True:
        select = selection()
        if select==1:
            add_category()
        elif select==2:
            append_category()
        elif select==3:
            check_budget()
        elif select==4:
            print("Exiting program\n")
            time.sleep(1)
            print(Fore.GREEN + "3\n")
            time.sleep(1)
            print(Fore.YELLOW + "2\n")
            time.sleep(1)
            print(Fore.RED + "1\n")
            time.sleep(1)
            print(Fore.LIGHTCYAN_EX + "Goodbye!")
            with open("Budget-Allocation/budget_data.json", "w") as json_file:
                json.dump(budgetdata, json_file)
            return
            

def selection(): 
    select=input("Would you like to: \n1.Add a new category and budget \n2.Append an existing categories budget \n3.Check a cost against a characters budget \n4.Exit \n\n")
    try:
        select = float(select)
    except:
        print(Fore.RED + "\nPlease enter a valid selection\n")
        select = selection()

    if select < 1 or select > 4:
        print(Fore.RED + Back.WHITE +"\nPlease enter a valid selection\n")
        select = selection()
    return select

def add_category():
    category = input("\nEnter the category you would like to add: \n")
    if category in budget_data:
        print(Fore.RED + "\nCategory already exists!\n")
        return
    budget = input("\nEnter the budget for this category: \n")
    try:
        budget = float(budget)
    except:
        print(Fore.RED + "\nPlease enter a valid budget\n")
        add_category()
    budget_data[category] = budget
    print(Fore.GREEN + "\nCategory added successfully!\n")

def append_category():
    Found = False
    category = input("Enter the category you would like to append: \n")

    if item not in categorylist:
        print(Fore.RED + "\nThe category was not found, check your spelling!\n")
        return
    
    try:
        budget = float(input("\nEnter the amount you would like to append: \n"))
        budget_data[category] += budget
        print(Fore.GREEN + "\nYour budget was appended!\n")
    except ValueError:
        print(Fore.RED + "\nPlease enter a valid amount!\n")

def check_budget():
    category = input("\nEnter the category you would like to check: \n")
    if category not in budget_data:
        print(Fore.RED + "\nCategory not found!\n")
        return

    try:
        cost = float(input("\nEnter the cost of the item: \n"))
        remaining_budget = budget_data[category] - cost
        if remaining_budget < 0:
            print(Fore.RED + "\nYou have exceeded your budget!\n")
            print(f"Over budget by: {-remaining_budget}")
        else:
            print(Fore.GREEN + "\nYou have not exceeded your budget!\n")
            print(f"Remaining budget: {remaining_budget}")
    except ValueError:
        print(Fore.RED + "\nPlease enter a valid cost!\n")

    raise ValueError(Fore.RED + "\nCategory not found!\n")

if __name__ == "__main__":
    print("Unit testing now! \n")
    main()