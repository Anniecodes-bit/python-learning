#Expense tracker project

ExpensesList = []#List of all expenses in form of dictionary
print("Welocome to expense Tracker:kam kharcha kara")

while True:
    print("====MENU====")
    print("1.Add Expense")
    print("2.view All Expenses")
    print("3.view total kharcha")
    print("4.Exit")

    choice=int(input("Please Enter your choice:"))
#ADD expense
    if(choice==1):
        date =input("kau date re kharcha karithila? :")
        category=input("kau type rae kharcha kala ?(food, Travel,Makeup,Books ):")
        description=input("Au detail re dia :")
        ammount=float(input("Enter the ammount ? :"))
        expense={
            "date":date,
            "category":category,
            "description":description,
            "ammount":ammount
        }
        ExpensesList.append(expense)
        print(" \n Done bro.Expense is add succesfully")
#2 View all expenses
    elif(choice==2):
        if(len(ExpensesList)==0):
            print("no expense added. jao aga kharcha kara.")
        else:
            print("=== AE ta hauchi apananka sabu expense=====")
            count=1 
            for eachKharcha in ExpensesList:
                print(f"kharcha Number {count} ->{eachKharcha["date"]},{eachKharcha["category"]},{eachKharcha["description"]},{eachKharcha["ammount"]}")
    
                count=count+1
#3.View total spending
    elif{choice==3}:
        total=0
        for eachkharcha in ExpensesList:
            total=total + eachkharcha["ammount"]

        print("\n TOTAL KHARCHA =" ,total)
#4 Exit
    elif(choice==4):
        print("Thank you apana amora system use kale")
        break
    else:
        print("INVALID CHOICE. TRY AGAIN") 