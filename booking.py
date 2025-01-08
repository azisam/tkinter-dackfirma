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
            "id": self.id,
            "date": self.date,
            "time": self.time,
            "service": self.service,
            "customer": self.customer
        }