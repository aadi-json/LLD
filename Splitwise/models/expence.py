from models.user import User
from models.group import Group
from decimal import Decimal

class Expence:
    def __init__(self, expence_id:int, description:str, amount:Decimal, paid_by:User, group:Group):
        self.expence_id = expence_id
        self.description = description
        self.amount = Decimal(amount)
        self.paid_by = paid_by
        self.group = group
        self.validate_expence()

    def validate_expence(self):
        if self.amount <= Decimal("0"):
            raise ValueError("The amount is less than 0")
        if self.paid_by.user_id not in self.group.members:
            raise ValueError("The user must belong to the group")

    def get_details(self):
        return {
            "expence_id": self.expence_id,
            "Description": self.description,
            "Amount": self.amount,
            "Paid_by": self.paid_by.name,
            "Group": self.group.name
        }


        
    