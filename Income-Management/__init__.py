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
      print("1.add income")
      print("2.get total income")
      print("3.Exit") 
      choice=input("enter whic option(1,2,3)")

      if choice == "1":
         source=(input("source of income:")) 
         amount=float(input("amount:"))
         add_income(source,amount)
      elif choice == "2":
          get_total_income()
      elif choice == "3":
          print("exiting icnome management menu...")
          break
      else:
          print("invalid option please try again and input options 1,2 or 3")
          
   
    

if __name__ == "__main__":
    main()


































