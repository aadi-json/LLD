from parking_floor import ParkingFloor
from parking_ticket import ParkingTicket

class ParkingLot:
    def __init__(self, name, pricing_strategy):
        self.name = name
        self.floors = []
        self.active_tickets = {}
        self.ticket_counter = 1
        self.pricing_strategy = pricing_strategy

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def find_available_spot(self, vehicle):
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle)

            if spot:
                return spot

        return None

    def park_vehicle(self, vehicle):
        if vehicle.number in self.active_tickets:
            raise Exception("Vehicle is already parked")

        spot = self.find_available_spot(vehicle)

        if spot is None:
            raise Exception("No parking spot available")

        spot.park_vehicle(vehicle)

        ticket = ParkingTicket(
            self.ticket_counter,
            vehicle,
            spot
        )

        self.active_tickets[vehicle.number] = ticket
        self.ticket_counter += 1

        return ticket

    def unpark_vehicle(self, vehicle_number):
        ticket = self.active_tickets.get(vehicle_number)

        if ticket is None:
            raise Exception("Vehicle is not parked")

        ticket.close_ticket()

        fee = self.pricing_strategy.calculate_price(ticket)

        ticket.spot.remove_vehicle()

        del self.active_tickets[vehicle_number]

        return ticket, fee