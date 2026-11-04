class User:
    def __init__(self, user_id:str, name:str):
        self.__user_id = user_id
        self.name = name

    @property
    def user_id(self) -> str:
        return self.__user_id 

