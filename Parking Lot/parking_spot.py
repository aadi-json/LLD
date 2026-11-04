from vehicle import Vehicle, VehicleType

class ParkingSpot:
    def __init__(self, spot_id: int, vehicle_type: VehicleType):
        self.spot_id = spot_id
        self.vehicle_type = vehicle_type
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def park_vehicle(self, vehicle: Vehicle):
        if not self.is_available():
            raise Exception("Parking spot is occupied")

        if self.vehicle_type != vehicle.vehicle_type:
            raise Exception("Vehicle type does not match")

        self.vehicle = vehicle

    def remove_vehicle(self):
        if self.is_available():
            raise Exception("Parking spot is already empty")

        self.vehicle = None