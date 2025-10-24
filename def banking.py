class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_number = self._generate_account_number()
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        
    def _generate_account_number(self):
        import random
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction = {
                'type': 'DEPOSIT',
                'amount': amount,
                'balance_after': self.balance
            }
            self.transaction_history.append(transaction)
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            transaction = {
                'type': 'WITHDRAWAL',
                'amount': amount,
                'balance_after': self.balance
            }
            self.transaction_history.append(transaction)
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        return self.transaction_history
    
    def display_account_info(self):
        print(f"\n=== Account Information ===")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")

class BankingApp:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self):
        print("\n=== Create New Account ===")
        name = input("Enter account holder name: ").strip()
        
        if not name:
            print("Name cannot be empty!")
            return
        
        initial_deposit = 0
        try:
            deposit_input = input("Enter initial deposit amount (default 0): ").strip()
            if deposit_input:
                initial_deposit = float(deposit_input)
                if initial_deposit < 0:
                    print("Initial deposit cannot be negative!")
                    return
        except ValueError:
            print("Invalid amount! Using default value 0.")
        
        account = BankAccount(name, initial_deposit)
        self.accounts[account.account_number] = account
        
        print(f"\nAccount created successfully!")
        print(f"Account Number: {account.account_number}")
        print(f"Account Holder: {account.account_holder}")
        print(f"Initial Balance: ${initial_deposit:.2f}")
    
    def find_account(self, account_number):
        return self.accounts.get(account_number)
    
    def deposit_money(self):
        print("\n=== Deposit Money ===")
        account_number = input("Enter account number: ").strip()
        
        account = self.find_account(account_number)
        if not account:
            print("Account not found!")
            return
        
        try:
            amount = float(input("Enter deposit amount: $"))
            if account.deposit(amount):
                print(f"Successfully deposited ${amount:.2f}")
                print(f"New balance: ${account.get_balance():.2f}")
            else:
                print("Invalid deposit amount!")
        except ValueError:
            print("Invalid amount!")
    
    def withdraw_money(self):
        print("\n=== Withdraw Money ===")
        account_number = input("Enter account number: ").strip()
        
        account = self.find_account(account_number)
        if not account:
            print("Account not found!")
            return
        
        try:
            amount = float(input("Enter withdrawal amount: $"))
            if account.withdraw(amount):
                print(f"Successfully withdrew ${amount:.2f}")
                print(f"New balance: ${account.get_balance():.2f}")
            else:
                print("Insufficient funds or invalid amount!")
        except ValueError:
            print("Invalid amount!")
    
    def check_balance(self):
        print("\n=== Check Balance ===")
        account_number = input("Enter account number: ").strip()
        
        account = self.find_account(account_number)
        if not account:
            print("Account not found!")
            return
        
        account.display_account_info()
    
    def view_transaction_history(self):
        print("\n=== Transaction History ===")
        account_number = input("Enter account number: ").strip()
        
        account = self.find_account(account_number)
        if not account:
            print("Account not found!")
            return
        
        history = account.get_transaction_history()
        if not history:
            print("No transactions found.")
            return
        
        print(f"\nTransaction History for {account.account_holder}:")
        for i, transaction in enumerate(history, 1):
            print(f"{i}. {transaction['type']}: ${transaction['amount']:.2f} | Balance: ${transaction['balance_after']:.2f}")
    
    def display_menu(self):
        print("\n" + "="*40)
        print("        SIMPLE BANKING APPLICATION")
        print("="*40)
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. View All Accounts")
        print("7. Exit")
        print("="*40)
    
    def view_all_accounts(self):
        print("\n=== All Accounts ===")
        if not self.accounts:
            print("No accounts found.")
            return
        
        for i, account in enumerate(self.accounts.values(), 1):
            print(f"{i}. {account.account_holder} - {account.account_number} - Balance: ${account.get_balance():.2f}")
    
    def run(self):
        print("Welcome to Simple Banking App!")
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-7): ").strip()
                
                if choice == '1':
                    self.create_account()
                elif choice == '2':
                    self.deposit_money()
                elif choice == '3':
                    self.withdraw_money()
                elif choice == '4':
                    self.check_balance()
                elif choice == '5':
                    self.view_transaction_history()
                elif choice == '6':
                    self.view_all_accounts()
                elif choice == '7':
                    print("Thank you for using Simple Banking App!")
                    break
                else:
                    print("Invalid choice! Please enter a number between 1-7.")
            
            except KeyboardInterrupt:
                print("\n\nApplication interrupted.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = BankingApp()
    app.run()