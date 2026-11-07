from models.user import User
from typing import Dict
class Group:
    def __init__(self, group_id:int, name:str):
        self.group_id = group_id
        self.name = name
        self.members: Dict[User] = {}

    def add_member(self, user:User):
        if user.user_id in self.members:
            raise Exception("User is already in the group")
        self.members[user.user_id] = user
        print(f"{user.name} is added to {self.name}")

    def remove_memeber(self, user:User):
        if user not in self.members:
            raise Exception
        del self.members[user.user_id]
        print(f"{user.name} is deleted from {self.name}")

    def get_members(self):
        return list(self.members.values())
    