from show import Show

class Theater:
    def __init__(self, theater_id:str, name:str, city:str) -> None:
        self.__theater_id = theater_id
        self.name = name
        self.city = city
        self.__shows:Show = []

    @property
    def theater_id(self):
        return self.__theater_id

    @property
    def shows(self):
        return tuple(self.__shows)

    def add_show(self, new_show:Show):
        self.__shows.append(new_show)