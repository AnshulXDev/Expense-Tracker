# GitHub - @codedrust


expenses=[]
##
print("=== Welcome to the Expense Tracker! ===")
##
while True:
    print("\nChoose one option (1-4): ")
    print("1. Add Expense(s)")
    print("2. View Expense(s) Total")
    print("3. View All Expense(s)")
    print("4. Exit")
    
    choice=input("Enter your choice: ")

#logic-easy
    if choice=="1":
        exp_name=input("Enter item's name: ")
        exp_amount=float(input("Enter amount: "))
#new--
        single_exp = {
            "name": exp_name,
            "amount": exp_amount
        }
        expenses.append(single_exp)
        print("Expense added successfully!")
    elif choice=="2":
        total=0
        for items in expenses:
            total += items["amount"]
        print(f"Total expenses: ₹{total}")
    elif choice=="3":
        if len(expenses)==0:
            print("No expenses found!")
        else:
            print("\n---All expenses---")
            for num, item in enumerate(expenses, start=1):
                print(f"{num}. {item["name"]}")
    elif choice=="4":
        print("\nExiting... Goodbye!")
        break
    else:
        print("Invalid option! Try again...")