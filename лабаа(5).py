
class Sneakers:
    
    def __init__(self, brand, price, quantity, numberOfSales):
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.numberOfSales = numberOfSales

    
class SportShoesStore:
    def __init__(self):
        self.inventory = []

    def add_sneakers(self, sneakers):
        self.inventory.append(sneakers)

    def sort_by_price(self):
        self.inventory.sort(key=lambda x: x.price, reverse=True)

    def sort_by_quantity(self):
        self.inventory.sort(key=lambda x: x.quantity, reverse=True)

    def top_sneakers(self, n=5):
         ''' Повертає топ-N кросівок за популярністю (за кількістю продажів).'''
        sorted_inventory = sorted(self.inventory, key=lambda x: x.numberOfSales, reverse=True)
        return sorted_inventory[:n]

    
def main():

    sneaker1 = Sneakers("Nike", 130, 60, 110)
    sneaker2 = Sneakers("Adidas", 90, 40, 90)

    store = SportShoesStore()
    store.add_sneakers(sneaker1)
    store.add_sneakers(sneaker2)

    print("Склад для сортування:")
    for sneaker in store.inventory:
        print(f"{sneaker.brand} - {sneaker.price}")

    store.sort_by_price()
    print("\nСклад після сортування за ціною:")
    for sneaker in store.inventory:
        print(f"{sneaker.brand} - {sneaker.price}")

    top_sneakers = store.top_sneakers()
    print("\nТоп 5 за популярністю:")
    for sneaker in top_sneakers:
        print(sneaker.brand)
        

if __name__ == "__main__":
    main()

