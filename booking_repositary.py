import json
from booking import Booking

class BookingRepositary:
    def __init__(self, filename):
        self.filename = filename

    # Hämta alla tillgängliga bokningstider (ej bokade)
    def get_available_bookings(self) -> list:
        with open(self.filename, "r", encoding="utf-8") as file:
            bookings = json.load(file) # Läser in bokningsdata från filen

        # Filtrerar ut bokningar som inte har någon kund kopplad (tillgängliga tider)
        available_bookings = []
        for booking in bookings:
            if not booking["customer"]: # Kontrollera om kunden är tom
                available_bookings.append(booking)
        
        return available_bookings # Returnerar listan med tillgängliga bokningstider

    # Hämta alla kundbokningar
    def get_customer_bookings(self) -> list:
        with open(self.filename, "r", encoding="utf-8") as file:
            bookings = json.load(file) # Läser in bokningsdata från filen

        # Filtrerar ut bokningar som har en kund kopplad
        customer_bookings = []
        for booking in bookings:
            if booking["customer"]: # Kontrollera om kunden finns
                customer_bookings.append(booking)
                
        return customer_bookings # Returnerar listan med kundbokningar

    # Boka en tid (Kund)
    def book_time(self, id: str, service: str, customer: dict):
        # Öppna JSON filen i läsläge
        with open(self.filename, "r", encoding="utf-8") as file:
            bookings = json.load(file) # Läser in bokningsdata från filen

        # Letar efter bokning med matchande ID
        for booking in bookings:
            if booking["id"] == id: # Kontrollera om ID matchar
                booking["service"] = service # Uppdatera tjänsten för bokningen
                booking["customer"] = customer # Koppla kunden till bokningen

                # Öppna JSON-filen i skrivläge för att spara ändringarna
                with open(self.filename, "w", encoding="utf-8") as file:
                    json.dump(bookings, file, ensure_ascii=False, indent=4) # Spara filen med formattering
                
                return booking # Returnera den uppdaterade bokningen

    # Lägg till en ny bokningstid (Ägare)
    def add_booking(self, booking) -> dict:
        with open(self.filename, "r", encoding="utf-8") as file:
            bookings = json.load(file) # Läser in bokningsdata från filen

            # Generera ett unikt boknings ID
            booking_id = int(bookings[len(bookings) - 1]["id"]) + 1 # Hämta senaste ID och öka med 1
            booking_id = str(booking_id)
            booking.set_id(booking_id) # Tilldela det nya ID:t till bokningen

            bookings.append(booking.dictionary()) # Lägg till den nya bokningen i listan

        # Spara den uppdaterade listan med bokningar till JSON-filen
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(bookings, file, ensure_ascii=False, indent=4)
            return booking # Returnera den tillagda bokningen

        return {} # Returnera en tom dictionary om något gick fel
