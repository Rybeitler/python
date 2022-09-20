class Store:
    def __init__(self, name):
        self.name = name
        self.products = {"sneaker": [], "dress": [], "athletic": []}
        self.id_nums = 1
        self.hidden = []

    def add_product(self, new_product):
        temp = []
        self.hidden.append(new_product)
        temp.append(new_product.name)
        temp.append(new_product.price)
        temp.append(self.id_nums)
        self.id_nums += 1
        self.products[new_product.category].append(temp)
        return self

    def inventory(self):
        print(f"Sneakers: {self.products['sneaker']}\nDress Shoes: {self.products['dress']}\nAthletic Shoes: {self.products['athletic']} ")

    def sell_product(self, id):
        for key in self.products:
            for prod in self.products[key]:
                if prod[2] == id:
                    self.products[key].remove(prod)
                    print(f"{prod[0]} has been sold")

    def inflation(self, percent_increase):
        for product in self.hidden:
            product.update_price(percent_increase, True)
            temp = product.name
            for key in self.products:
                for prod in self.products[key]:
                    if temp == prod[0]:
                        prod[1] = product.price

    def set_clearance(self, percent_decrease):
        for product in self.hidden:
            product.update_price(percent_decrease, False)
            temp = product.name
            for key in self.products:
                for prod in self.products[key]:
                    if temp == prod[0]:
                        prod[1] = product.price