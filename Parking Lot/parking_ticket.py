from datetime import datetime

class ParkingTicket:
    def __init__(self, ticket_id, vehicle, spot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()
        self.exit_time = None

    def close_ticket(self):
        self.exit_time = datetime.now()

    def get_duration(self):
        if self.exit_time is None:
            raise Exception("Ticket is still active")

        return self.exit_time - self.entry_time