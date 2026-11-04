from enum import Enum

class VehicleType(Enum):
    BIKE = "BIKE"
    CAR = "CAR"
    TRUCK = "TRUCK"

class Vehicle:
    def __init__(self, number: str, vehicle_type: VehicleType):
        self.number = number
        self.vehicle_type = vehicle_type