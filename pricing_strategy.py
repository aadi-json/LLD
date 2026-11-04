from abc import ABC, abstractmethod
import math
from vehicle import VehicleType

class PricingStrategy(ABC):

    @abstractmethod
    def calculate_price(self, ticket):
        pass

class HourlyPricing(PricingStrategy):

    def calculate_price(self, ticket):
        duration = ticket.get_duration()

        hours = math.ceil(
            duration.total_seconds() / 3600
        )

        rates = {
            VehicleType.BIKE: 20,
            VehicleType.CAR: 50,
            VehicleType.TRUCK: 100
        }

        rate = rates[ticket.vehicle.vehicle_type]

        return hours * rate