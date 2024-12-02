



def show_balance(balance):
    print("***********************")

    print(f"your balance is {balance:.2f}$")
    print("***********************")


def deposit():
    print("***********************")

    amount = float(input("enter amount to deposit: "))
    print("***********************")

    if amount <= 0:
        print("***********************")

        print("amount must be greater than zero")
        print("***********************")

        return 0
    else:
        return amount
def withdraw(balance):
    print("***********************")
    amount = float(input("Enter amount to withdraw: "))
    print("***********************")
    if amount > balance:
        print("***********************")
        print("Insufficient balance")
        print("***********************")
        return 0
    elif amount <= 0:  # Fixed the condition
        print("***********************")
        print("Withdrawal amount must be positive")
        print("***********************")
        return 0
    else:
        print(f"your amount of {amount:.2f}$ has been withdrawn check the New balance")
        return amount

def main():

    balance= 0
    is_running = True
    while is_running:
        print("***********************")
        print("----banking program----")
        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        print("***********************")
        choice = input("Enter your choice (1 to 4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance+=deposit()
        elif choice == "3":
            balance-=withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("***********************")
            print("Invalid choice")
            print("***********************")

    print("***********************")

    print("Thank You Have a nice day!")

    print("***********************")

if __name__ == "__main__":
    main()
