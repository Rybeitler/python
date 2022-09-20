import product
import store


vans = product.Product("Vans", 70, "sneaker")
toms = product.Product("Toms", 40, "sneaker")
gucci = product.Product("Gucci", 1000, "dress")
nike = product.Product("Nike", 100, "athletic")

shoe_store= store.Store("shoe_store")
shoe_store.add_product(vans).add_product(toms).add_product(gucci).add_product(nike)

shoe_store.inventory()
shoe_store.set_clearance(10)


shoe_store.inventory()

shoe_store.sell_product(3)



