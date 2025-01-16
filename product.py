class Product:
    # Konstruktor för att initiera ett produktobjekt med dess egenskaper
    def __init__(self, id: str, name: str, price: int, in_stock: int, category: str):
        self.id = id # Unikt ID för produkten
        self.name = name # Produktens namn
        self.price = price # Produktens pris
        self.in_stock = in_stock # Antal enheter av produkten som finns i lager
        self.category = category # Kategori som produkten tillhör

    # Skapar en strängrepresentation av produktobjektet
    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Price: {self.price}, In stock: {self.in_stock}, Category: {self.category}'

    # Produktobjekt till dictionary
    def dictionary(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "inStock": self.in_stock,
            "category": self.category
        }
