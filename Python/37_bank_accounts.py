class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"The balance after deposit is {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"The balance after withdraw is {self.balance}")

    def display_balance(self):
        print(f"The balance is {self.balance}")

account = BankAccount("John", "Smith", "123456", "Bob", 10000, 0)
account.deposit(96)
account.withdraw(25)
account.display_balance()