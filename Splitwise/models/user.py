class User:
    def __init__(self, user_id:str, email:str, name:str):
        self.user_id  = user_id
        self.email = email
        self.name = name

    def __str__(self):
        return f"User_Id: {self.user_id} Email: {self.email} Name: {self.name}"
