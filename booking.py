class Booking:
    # Konstruktor för att initiera ett bokningsobjekt med datum och tid
    def __init__(self, date: str, time: str):
        self.id = "" # Unikt ID för bokningen, initialt tom
        self.date = date # Datum för bokningen
        self.time = time # Tid för bokningen
        self.service = "" # Tjänst kopplad till bokningen, initialt tom
        self.customer = {} # Dict för att lagra kunduppgifter, initialt tom

    # Skapar en strängrepresentation av bokningsobjektet
    def __str__(self):
        return f'ID: {self.id}, Date: {self.date}, Time: {self.time}, Service: {self.service}, Customer: {self.customer}'

    # Sätter det unika identifieringsnumret för bokningen
    def set_id(self, id: str):
        self.id = id

    # Bokningsobjekt till dictionary
    def dictionary(self):
        return {
            "id": self.id,
            "date": self.date,
            "time": self.time,
            "service": self.service,
            "customer": self.customer
        }
