from models.user import User
from decimal import Decimal

class ExpenceSplit:
    def __init__(self, user:User, amount:Decimal):
        self.user = user
        self.amount = Decimal(amount)
        self.validate_amount()

    def validate_amount(self):
        if self.amount < Decimal("0"):
            raise ValueError("Amount is less than 0")

    def get_details(self):
        return{
            "user": self.user,
            "Amount": self.amount
        }