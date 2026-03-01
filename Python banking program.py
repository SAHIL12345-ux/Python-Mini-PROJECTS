# Banking System

def show_balance(balance):
    print(f"Your balance is ₹{balance:.2f}")


def deposit(balance):
    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Invalid amount")
            return balance

        balance += amount
        print("Deposit successful!")

    except ValueError:
        print("Please enter a valid number!")

    return balance


def withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount")

        elif amount > balance:
            print("Insufficient balance")

        else:
            balance -= amount
            print("Withdrawal successful!")

    except ValueError:
        print("Please enter a valid number!")

    return balance


def menu():
    print("\n===== Banking Program =====")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def main():

    balance = 0

    while True:

        menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance = deposit(balance)

        elif choice == '3':
            balance = withdraw(balance)

        elif choice == '4':
            print("Thank you! Have a nice day!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
