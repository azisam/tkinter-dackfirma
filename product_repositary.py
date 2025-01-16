import json

class ProductRepositary:
    def __init__(self, filename):
        self.filename = filename # Filnamn där produktdata lagras

    # Hämta alla produkter
    def get_products(self) -> list:
        with open(self.filename, "r", encoding="utf-8") as file:
            products = json.load(file) # Läser in alla produkter från JSON filen
        
        return products # Returnerar listan
    
    # Lägg till en ny produkt
    def add_product(self, product) -> dict:
        with open(self.filename, "r", encoding="utf-8") as file:
            products = json.load(file) # Läser in befintliga produkter från JSON filen

        # Lägger till den nya produkten (som en dictionary) i produktlistan
        products.append(product.dictionary())

        with open(self.filename, "w", encoding="utf-8") as file:
            # Sparar den uppdaterade listan till filen
            json.dump(products, file, ensure_ascii=False, indent=4)
            return product.dictionary() # Returnerar den tillagda produkten

    # Ta bort en produkt baserat på dess ID
    def remove_product(self, id: str) -> dict:
        with open(self.filename, "r", encoding="utf-8") as file:
            products = json.load(file) # Läser in befintliga produkter från JSON filen
        
        for product in products:
            if id == product["id"]: # Letar efter en produkt med matchande ID
                products.remove(product) # Tar bort produkten från listan
        
                with open(self.filename, "w", encoding="utf-8") as file:
                    # Sparar den uppdaterade listan till filen
                    json.dump(products, file, ensure_ascii=False, indent=4)
                    return product # Returnerar den borttagna produkten
        
        return {} # Returnerar en tom dictionary om produkten inte hittades

    # Uppdatera en befintlig produkt
    def update_product(self, id: str, data: dict) -> dict:
        with open(self.filename, "r", encoding="utf-8") as file:
            products = json.load(file) # Läser in befintliga produkter från JSON filen
        
        for product in products:
            # Kontrollera om produkten med det angivna ID finns
            if id == product["id"]:
                product.update(data) # Uppdaterar produkten med ny data

                # Sparar den uppdaterade listan till filen
                with open(self.filename, "w", encoding="utf-8") as file:
                    json.dump(products, file, ensure_ascii=False, indent=4)
                    return product # Returnerar den uppdaterade produkten
    
        return {} # Returnerar en tom dictionary om produkten inte hittades
