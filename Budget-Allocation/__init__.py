def main():
    inpCategory = input("What is your category? \n")
    inpAmount = int(input("What is your amount? \n"))
    check_budget(inpCategory, inpAmount)

def set_budget(category, limit):
    pass

def check_budget(category, amount):
    print(category, amount)

if __name__ == "__main__":
    print("Unit testing now!")
    main()