from enum import Enum
from user import User
from movie import Movie
from seat import Seat
from show import Show
from payment_statergy import PaymentStatergy

class BookingStatus(Enum):
    CONFIRMED = 'CONFIRMED'
    CANCELLED = 'CANCELLED'

class Booking:
    booking_counter = 1

    def __init__(self, user:User, show:Show, seat:Seat ):
        self.__booking_id = self.booking_counter
        self.booking_counter +=1
        self.seat = tuple(seat)
        self.user = user
        self.show = show

        self.amount = len(seat) * show.price
        self.__status = BookingStatus.CONFIRMED

    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def status(self):
        return self.__status

    @classmethod
    def create_booking(cls, user: User, show: Show, seats: list, payment_statergy: PaymentStatergy):
        show.book_seat(seats)

        amount = len(seats) * show.price

        try:
            payment_success = payment_statergy.pay(amount)

            if not payment_success:
                raise Exception("Payment Failed")

        except Exception:
            show.release_seat(seats)
            raise
        return cls(user, show, seats)

    def cancle_booking(self):
        if self.__status == BookingStatus.CANCELLED:
            raise Exception("Booking is already cancelled")
        self.show.release_seat(self.seat)
        self.__status = BookingStatus.CANCELLED

    