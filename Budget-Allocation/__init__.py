import json

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
        elif select==4:
            jsontesting()
            selected=True
        else:
            print("Please enter a valid selection")
            select = selection()

def jsontesting():
    print("Testing")
    food_ratings = {"Pizza": 5, "Burger": 4, "Pasta": 3}
    json.dumps(food_ratings)


def selection(): 
    select=int(input("Would you like to: \n1.Add a new category and budget \n2.Append an existing categories budget \n3.Check a cost against a characters budget \n4.JSON Testing \n"))
    return select

def add_category():
    category = input("Enter the category you would like to add: \n")
    budget = int(input("Enter the budget for this category: \n"))

def append_category():
    category = input("Enter the category you would like to append: \n")
    budget = int(input("Enter the amount you would like to append: \n"))

def check_budget():
    category = input("Enter the category you would like to check: \n")
    cost = int(input("Enter the cost of the item: \n"))

if __name__ == "__main__":
    print("Unit testing now!")
    try:
        main()
    except:
        print("Error in main function")