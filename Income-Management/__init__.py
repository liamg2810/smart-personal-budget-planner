income_list=[]

def add_income():
    source=(input("source of income:"))
    amount=float(input("amount:"))
    
    income_dictionary={'source':source,'amount':amount}
    income_list.append(income_dictionary)


def get_total_income():
    for income_dictionary in income_list:
        print(income_dictionary["amount"])
        total=0




def main():
    while True:
      print("\nincome managment menu:\n")
       

   
   
   
    add_income()
    add_income()
    get_total_income()

if __name__ == "__main__":
    main()


































