class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"${amount} has been deposited. Your new balance is ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"${amount} has been withdrawn. Your new balance is ${self.balance}"
        else:
            return "Insufficient funds. Withdrawal failed."

def main():
    atm = ATM()
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Please select an option: ")

        if choice == "1":
            print(atm.check_balance())
        elif choice == "2":
            amount = float(input("Enter the deposit amount: $"))
            print(atm.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: $"))
            print(atm.withdraw(amount))
        elif choice == "4":
            print("Thank you for using this ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
