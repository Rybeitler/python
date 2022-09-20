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
        print(f"your Balance is: {self.balance}")
        return self
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def print_all(cls):
        for account in cls.all_accounts:
            print(f"Balance: {account.balance}, Intrest Rate: {account.int_rate}")

class user:
    def __init__(self, first_name, last_name, email, age, rate=2, balance=0):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = bank_account(rate, balance)
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
    def enroll(self):
        if self.is_rewards_member == True:
            print("Already a member1")
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
            return self
        else:
            print("Not enough points!")
            return self
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self
    def transfer_money(self, amount, other_user):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self


bob = user("bob", "belcher", "burgerman@gmail.com", 42,)
jack = user("jack", "shepard", "commanderShepard@gmail.com", 30, 5, 1000)

jack.make_deposit(100)
jack.display_user_balance()
bob.make_withdrawl(100)
bob.display_user_balance()

jack.transfer_money(200, bob)
jack.display_user_balance()
bob.display_user_balance()