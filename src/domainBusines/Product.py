class Product:
    def __init__(self, id, name, price, units):
        self.id = id
        self.name = name
        self.price = price
        self.units = units

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nPrice: ${self.price}\nUnits: {self.units}"