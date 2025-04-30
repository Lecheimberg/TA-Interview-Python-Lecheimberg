import bank_account
import sys

class BankApplication:
    def __init__(self):
        self.accounts = []

    def start(self):
        num_accounts = self.get_number_of_accounts()

        for _ in range(num_accounts):
            account = self.create_account_interactive()
            self.accounts.append(account)

        while True:
            self.perform_transfer()
            continue_transfers = input("Do you want to perform another transfer? (yes/no): ")
            if continue_transfers.lower() != 'yes':
                print("Exiting the application.")
                sys.exit()

    def get_number_of_accounts(self):
        while True:
            try:
                num_accounts = int(input("Enter the number of accounts to create (1-5): "))
                if 1 <= num_accounts <= 5:
                    return num_accounts
            except ValueError:
                pass
            print("Invalid input. Please enter a number between 1 and 5.")

    def create_account(self, name, number, balance):
        account = bank_account.BankAccount(name, number, balance)
        self.accounts.append(account)
        return account

    def create_account_interactive(self):
        account_holder_name = input("Enter account holder's name: ")
        account_number = input("Enter account number: ")
        while True:
            try:
                balance = float(input("Enter initial balance: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid balance.")
        return self.create_account(account_holder_name, account_number, balance)

    def perform_transfer(self):
        print("Select the account to transfer from:")
        from_account = self.select_account()

        print("Select the account to transfer to:")
        to_account = self.select_account()

        while True:
            try:
                amount = float(input("Enter the amount to transfer: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        from_account_starting_balance = from_account.get_balance()
        to_account_starting_balance = to_account.get_balance()

        if from_account.withdraw(amount):
            to_account.deposit(amount)

            print("Transfer successful!")
            print(f"Account {from_account.get_account_number()} starting balance: ${from_account_starting_balance}")
            print(f"Account {from_account.get_account_number()} ending balance: ${from_account.get_balance()}")
            print(f"Account {to_account.get_account_number()} starting balance: ${to_account_starting_balance}")
            print(f"Account {to_account.get_account_number()} ending balance: ${to_account.get_balance()}")
        else:
            print("Transfer failed. Insufficient funds.")

    def select_account(self):
        for idx, account in enumerate(self.accounts, start=1):
            print(f"{idx}. {account.get_account_holder_name()} - {account.get_account_number()}")

        while True:
            try:
                account_index = int(input(f"Select an account (1-{len(self.accounts)}): ")) - 1
                if 0 <= account_index < len(self.accounts):
                    return self.accounts[account_index]
            except ValueError:
                pass
            print("Invalid input. Please select a valid account number.")

if __name__ == "__main__":
    app = BankApplication()
    app.start()
