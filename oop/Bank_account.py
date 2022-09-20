class bank_account:
    all_accounts = []
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate * 0.01
        self.balance = balance
        bank_account.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if (self.balance - amount > 0):
            self.balance -= amount
            return self
        else:
            print("Insufficent funds. Charging a $5 fee")
            self.balance -= (amount + 5)
            return self
    def display_account_info(self):
        print(f"Your Balance is: {self.balance}")
        return self
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def print_all(cls):
        for account in cls.all_accounts:
            print(f"Balance: {account.balance}, Intrest Rate: {account.int_rate}")


account1 = bank_account(1)
account2 = bank_account(5, 1000)

account1.deposit(100).withdraw(200).deposit(100).deposit(100).yield_interest().display_account_info()
account2.yield_interest().display_account_info()
bank_account.print_all()