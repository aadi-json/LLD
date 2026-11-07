from abc import ABC, abstractmethod
from decimal import Decimal
from models.user import User
from typing import List
from models.expense_split import ExpenceSplit

class SplitStatergy:
    @abstractmethod
    def split(self, participants:List[User], amount:Decimal):
        pass