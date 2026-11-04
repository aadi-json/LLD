from parking_spot import ParkingSpot
from vehicle import Vehicle

class ParkingFloor:
    def __init__(self, floor_number: int):
        self.floor_number = floor_number
        self.spots = []

    def add_spot(self, spot: ParkingSpot):
        self.spots.append(spot)

    def find_available_spot(self, vehicle: Vehicle):
        for spot in self.spots:
            if (
                spot.is_available()
                and spot.vehicle_type == vehicle.vehicle_type
            ):
                return spot

        return None