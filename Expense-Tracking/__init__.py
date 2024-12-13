def add_expense(category, amount):
    print(category, amount)
def get_total_expenses():
    pass

def get_expenses_by_category(category):
    pass

def main():
    amount = input("userr money value \n")
    category = input("What category are you using? \n")
    try:
        add_expense(category, amount)
    except:
        print("Error")

main()