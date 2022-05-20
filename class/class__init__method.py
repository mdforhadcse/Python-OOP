class Item:
    def __init__(self, name: str, price: float, quantity=0):  # automatically execute this method
        # print(f'Instance created: {name}')
        # validation
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assigning self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
        # return x * y


item1 = Item("Phone", 15000)
# item1.name = "Phone" This job is done by "self.name = name"
# item1.price = 15000
# item1.quantity = 5

item2 = Item("Laptop", 40000, 3)
# item2.name = "Laptop" This job is done by "self.name = name"
# item2.price = 40000
# item2.quantity = 3

print(item2.calculate_total_price())

# print(item1.name)
# print(item2.name)
# print(item1.price)
# print(item2.price)
# print(item1.quantity)
# print(item2.quantity)
