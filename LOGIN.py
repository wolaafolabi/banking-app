# trial 1 of the banking app

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def savings_account():
    def show_Balance():
         print(f"Your balance is ${Balance:.2f}")
    Balance = 5000000000
    is_running = True

    while is_running:
        print("WELCOME TO YOUR SAVINGS")
        print("WHAT WOULD YOU LIKE TO DO TODAY")
        print("1.Show Balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.Exit") 

        choice=input("enter your choice (1-4): ")

        if choice=="1":
            show_Balance()
        elif choice=="2":
            Balance += deposit()
        elif choice=="3":
            Balance -= withdraw()
        elif choice=="4":
            is_running=False
        else:
            print("That is not a valid choice")

def deposit():
    amount = float(input("Enter an amount to be deposited"))
    if amount<0:
        print("amount is invalid")
        return 0
    else:
        return amount        

def withdraw():
    amount = float(input("How much do you want to withdraw"))

    if amount > balance:
        print("INSUFICIENT FUNDS!!!")
        return 0
    elif amount < 0:
        print("Amount must be more than 0")
        return 0
    else:
        return amount

print("*************************************************************")
print("WELCOME TO X FUNDS")

# Predefined username and password
correct_username = "TOGBE"
correct_password = "12345678"

# User input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Authentication check
if username == correct_username and password == correct_password:
    print("Login successful!")
    print("*************************************************************")
    print("WELCOME TOGBE!")
    print("WHAT WOULD YOU LIKE TO DO TODAY")
    print("*************************************************************")

# Main Home page
    balance = 1000000000
    is_running = True

    while is_running:
        print("1.Show Balance")
        print("2.Savings Account")
        print("3.deposit")
        print("4.withdraw")
        print("5.Exit") 
        print("*************************************************************")


        choice=input("enter your choice (1-5): ")

        if choice=="1":
            show_balance()
        elif choice=="2":
            savings_account()
        elif choice=="3":
            balance += deposit()
        elif choice=="4":
            balance -= withdraw()
        elif choice=="5":
            is_running=False
        else:
            print("That is not a valid choice")
    print("THANK YOU FOR BANKING WITH US!")
    print("HAVE A NICE DAY")
    print("*************************************************************")

        
else:
    print("Login failed! Please check your username and password.")
    print("*************************************************************")
