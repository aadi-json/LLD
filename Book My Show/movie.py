class Movie:
    def __init__(self, movie_id:str, name:str, duration:float):
        self.__movie_id = movie_id
        self.name = name
        self.duration = duration

    @property
    def movie_id(self) -> str:
        return self.__movie_id