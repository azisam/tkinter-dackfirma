import json
from booking import Booking

class BookingRepositary:
    def __init__(self, filename):
        self.filename = filename
        # kanske checka ifall json filen existerar och om inte skapa den
    
    def get_available_bookings(self) -> list:
        with open(self.filename, "r") as file:
            bookings = json.load(file)

        # Filtrerar ut (tar bort) redan bokade tider från listan
        available_bookings = []
        for booking in bookings:
            if not booking["customer"]:
                available_bookings.append(booking)
        
        return available_bookings
    
    def get_customer_bookings(self) -> list:
        with open(self.filename, "r") as file:
            bookings = json.load(file)

        # Filtrerar bokningar med kunder
        customer_bookings = []
        for booking in bookings:
            if booking["customer"]:
                customer_bookings.append(booking)
                
        return customer_bookings

    # Boka en tid (kund)
    def book_time(self, id: str, service: str, customer: dict):
        # Öppna JSON filen i läsläge
        with open(self.filename, "r") as file:
            bookings = json.load(file)

        # Loop:a igenom och leta efter matchande ID
        for booking in bookings:
            if booking["id"] == id:
                booking["service"] = service
                booking["customer"] = customer

                # Öppna JSON filen i skrivläge
                with open(self.filename, "w") as file:
                    # Sparar till JSON filen med lättläst formattering
                    json.dump(bookings, file, ensure_ascii=False, indent=4)
                
                return booking
