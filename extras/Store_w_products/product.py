class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self. category = category
    
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * (percent_change * 0.01)
            return self
        else:
            self.price -= self.price * (percent_change * 0.01)
            return self

    def __repr__(self):
        return f"Product: {self.name}, Price: {self.price}, Category: {self.category}"

    def print_info(self):
        print(f"Product: {self.name}\nPrice: {self.price} \nCategory: {self.category}")