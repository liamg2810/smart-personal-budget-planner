def main():
    select = selection()
    selected = False
    while selected==False:
        if select==1:
            add_category()
            selected=True
        elif select==2:
            append_category()
            selected=True
        elif select==3:
            check_budget()
            selected=True
        else:
            print("Please enter a valid selection")
            select = selection()




def selection(): 
    select=int(input("Would you like to: \n1.Add a new category and budget \n2.Append an existing categories budget \n3.Check a cost against a characters budget"))
    return select

def add_category():
    category = input("Enter the category you would like to add: ")
    budget = int(input("Enter the budget for this category: "))

def append_category():
    category = input("Enter the category you would like to append: ")
    budget = int(input("Enter the amount you would like to append: "))

def check_budget():
    category = input("Enter the category you would like to check: ")
    cost = int(input("Enter the cost of the item: "))

if __name__ == "__main__":
    print("Unit testing now!")
    main()