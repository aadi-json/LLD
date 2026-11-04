from datetime import datetime

from user import User
from movie import Movie
from theater import Theater
from seat import Seat, SeatType
from show import Show
from booking import Booking
from payment_statergy import UPI, Card


# Create user
user = User(1, "Aditya")


# Create movie
movie = Movie(1, "Avengers: Endgame", 180)


# Create seats
seat1 = Seat(1, SeatType.REGULAR)
seat2 = Seat(2, SeatType.PREMIUM)
seat3 = Seat(3, SeatType.REGULAR)


# Create show
show = Show(
    1,
    movie,
    datetime.now(),
    200,
    [seat1, seat2, seat3]
)


# Create theatre
theatre = Theater(1, "PVR Cinemas", "Pune")
theatre.add_show(show)


# Display available seats
print("Available seats:")

for seat in show.get_available_seats():
    print(seat.seat_id, seat.seat_type.value)


# Select seats
selected_seats = [seat1, seat2]


# Select payment method
payment = UPI()

# Alternatively:
# payment = CardPayment()


# Create booking
booking = Booking.create_booking(
    user,
    show,
    selected_seats,
    payment
)


# Display booking details
print("\nBooking confirmed!")

print("Booking ID:", booking.booking_id)
print("User:", booking.user.name)
print("Movie:", booking.show.movie.name)
print("Amount:", booking.amount)
print("Status:", booking.status.value)


# Display seats after booking
print("\nAvailable seats after booking:")

for seat in show.get_available_seats():
    print(seat.seat_id)


# Cancel booking
booking.cancle_booking()

print("\nBooking cancelled successfully!")


# Display seats after cancellation
print("\nAvailable seats after cancellation:")

for seat in show.get_available_seats():
    print(seat.seat_id)