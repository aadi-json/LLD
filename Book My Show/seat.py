from enum import Enum

class SeatType(Enum):
    REGULAR = "REGULAT"
    PREMIUM = "PREMIUM"

class Seat:
    def __init__(self, seat_id:str, seat_type:SeatType):
        self.__seat_id = seat_id
        self.seat_type = seat_type

    @property
    def seat_id(self):
        return self.__seat_id

    