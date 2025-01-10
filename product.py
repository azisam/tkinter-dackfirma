class Product:
    def __init__(self, id: str, name: str, price: int, in_stock: int, category: str):
        self.id = id
        self.name = name
        self.price = price
        self.in_stock = in_stock
        self.category = category

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Price: {self.price}, In stock: {self.in_stock}, Category: {self.category}'

    def dictionary(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "inStock": self.in_stock,
            "category": self.category
        }
