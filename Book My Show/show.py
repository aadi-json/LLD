from movie import Movie
from seat import Seat
from typing import List
class Show:
    def __init__(
            self, 
            show_id:str,
            movie:Movie, 
            start_time:str, 
            price:float, 
            seats: int
        ):
        self.__show_id = show_id
        self.movie = movie
        self.start_time = start_time
        self.price = price

        self.__seats = tuple(seats)
        self.__booked_seat = set()

    @property
    def show_id(self):
        return self.__show_id

    @property
    def seat(self):
        return self.__seats

    def get_available_seats(self) -> List[Seat]:
        return [
            seat for seat in self.__seats
            if seat.seat_id not in self.__booked_seat
        ]

    def book_seat(self, seats:Seat):
        if not seats:
            raise ValueError("Please select the seat")

        selected_ids = [seat.seat_id for seat in seats]

        if len(selected_ids) != len(set(selected_ids)):
            raise ValueError("Duplicate seat is selected")

        valid_seat_ids = {seat.seat_id for seat in self.__seats}

        for seat in seats:
            if seat.seat_id not in valid_seat_ids:
                raise ValueError(f"It's valid: {seat.seat_id}")

            if seat.seat_id in self.__booked_seat:
                raise ValueError("Seat is already booked")
            
        for seat in seats:
            self.__booked_seat.add(seat.seat_id)
        print("DEBUG - Booked seat IDs:", self.__booked_seat)
            
    def release_seat(self, seats:Seat):
        for seat in seats:
            self.__booked_seat.discard(seat.seat_id)
    

        


