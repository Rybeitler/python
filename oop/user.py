class user:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
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


guy1 = user("bob", "belcher", "burgerman@gmail.com", 42)

guy1.display_info().enroll().enroll().spend_points(500).spend_points(100).display_info()
