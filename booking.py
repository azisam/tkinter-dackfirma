class Booking:
    def __init__(self, id: str, date: str, time: str):
        self.id = id
        self.date = date
        self.time = time
        self.service = ""
        self.customer = {}

    def __str__(self):
        ...

    def dictionary(self):
        return {
            "bookingID": self.booking_id,
            "date": self.date,
            "time": self.time,
            "service": self.service,
            "isBooked": self.isBooked,
            "customer": {} # {"firstName": "Joe", "lastName": "Doe", "email": "joe.doe@email.com"}
        }