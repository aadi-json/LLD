from vehicle import Vehicle, VehicleType
from parking_spot import ParkingSpot
from parking_floor import ParkingFloor
from parking_lot import ParkingLot
from pricing_strategy import HourlyPricing


# Create parking lot
parking_lot = ParkingLot(
    "City Parking",
    HourlyPricing()
)

# Create floor
floor1 = ParkingFloor(1)

# Add parking spots
floor1.add_spot(ParkingSpot(101, VehicleType.BIKE))
floor1.add_spot(ParkingSpot(102, VehicleType.CAR))
floor1.add_spot(ParkingSpot(103, VehicleType.TRUCK))

parking_lot.add_floor(floor1)

# Create vehicles
car = Vehicle("MH-01-1234", VehicleType.CAR)
bike = Vehicle("MH-01-5678", VehicleType.BIKE)

# Park car
car_ticket = parking_lot.park_vehicle(car)

print("Car parked successfully")
print("Ticket ID:", car_ticket.ticket_id)
print("Spot ID:", car_ticket.spot.spot_id)

# Park bike
bike_ticket = parking_lot.park_vehicle(bike)

print("\nBike parked successfully")
print("Ticket ID:", bike_ticket.ticket_id)
print("Spot ID:", bike_ticket.spot.spot_id)

# Unpark car
ticket, fee = parking_lot.unpark_vehicle("MH-01-1234")

print("\nCar exited successfully")
print("Entry Time:", ticket.entry_time)
print("Exit Time:", ticket.exit_time)
print("Parking Fee:", fee)