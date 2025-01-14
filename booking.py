class Booking:
    def __init__(self, date: str, time: str):
        self.id = ""
        self.date = date
        self.time = time
        self.service = ""
        self.customer = {}

    def __str__(self):
        return f'ID: {self.id}, Date: {self.date}, Time: {self.time}, Service: {self.service}, Customer: {self.customer}'

    def set_id(self, id: str):
        self.id = id

    def dictionary(self):
        return {
            "id": self.id,
            "date": self.date,
            "time": self.time,
            "service": self.service,
            "customer": self.customer
        }