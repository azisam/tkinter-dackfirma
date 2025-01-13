import json

class ProductRepositary:
    def __init__(self, filename):
        self.filename = filename

    # Hämta alla produkter
    def get_products(self) -> list:
        with open(self.filename, "r") as file:
            products = json.load(file)
        
        return products
    
    # Lägg till en ny produkt
    def add_product(self, product) -> dict:
        with open(self.filename, "r") as file:
            products = json.load(file)

        # Lägg till det nya produkten som en dictionary i produkter listan
        products.append(product.dictionary())

        with open(self.filename, "w") as file:
            json.dump(products, file, ensure_ascii=False, indent=4)
            return product.dictionary()

    # Ta bort en produkt
    def remove_product(self, id: str) -> dict:
        with open(self.filename, "r") as file:
            products = json.load(file)
        
        for product in products:
            if id == product["id"]:
                products.remove(product)
                deleted_product = product
        
        with open(self.filename, "w") as file:
            json.dump(products, file, ensure_ascii=False, indent=4)
            return deleted_product

    # Uppdatera en produkt
    def update_product(self, id: str, data: dict) -> dict:
        with open(self.filename, "r") as file:
            products = json.load(file)
        
        for product in products:
            # Kontrollera om ID matchar
            if id == product["id"]:
                # Uppdaterar produkten med ny data
                product.update(data)

                with open(self.filename, "w") as file:
                    json.dump(products, file, ensure_ascii=False, indent=4)
                    return product
