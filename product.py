class Product:
    def __init__(self, id: str, name: str, price: float, inStock: int, category: str):
        self.id = id
        self.name = name
        self.price = price
        self.inStock = inStock
        self.category = category

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Price: {self.price}, inStock: {self.inStock}, Category: {self.category}'

    def dictionary(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "inStock": self.inStock,
            "category": self.category
        }
