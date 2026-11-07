from models.user import User
from models.expense_split import ExpenceSplit
from decimal import Decimal
from typing import List
from statergies.split_statergy import SplitStatergy

class EqualSplit(SplitStatergy):
    def split(self, amount:Decimal, participants:List[User]) -> list[ExpenceSplit]:
        if not participants:
            raise ValueError("Participants cannot be empty")
        if amount <= Decimal("0"):
                raise ValueError("Not enough amount")

        #this will help you to convert rupee to paise to distribute amount equally
        total_paisa = int(amount * 100)
        # print(total_paisa)
      
    
        base_share, remainder = divmod(total_paisa, len(participants))
        # print(base_share, remainder)
        split = []
        for index, user in enumerate(participants):
            share = base_share
            print(index, user)
            if index < remainder:
                share +=1
            
    
            split_money = Decimal(share) / Decimal("100")
            # print(split_money)
            split.append(ExpenceSplit(user, split_money))
        return split
    