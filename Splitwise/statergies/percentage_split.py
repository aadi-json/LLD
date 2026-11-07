from models.user import User
from models.group import Group 
from decimal import Decimal
from  decimal import ROUND_DOWN
from typing import List, Dict
from models.expense_split import ExpenceSplit
from statergies.split_statergy import SplitStatergy

class PercentageSplit(SplitStatergy):
    def split(
            self,
            amount:Decimal,
            participant: List[User],
            percentage: Dict[int, Decimal]
    ) -> List[ExpenceSplit]:
        if not participant:
            raise ValueError("Participants are required")

        if amount <= Decimal("0"):
            raise ValueError("Amount cannot be zero")

        participant_ids = {user.user_id for user in participant}

        if set(percentage.keys()) != participant_ids:
            raise ValueError("Percentage must be provided for every user")

        total_percentage = sum(
        (Decimal(value)) for value in percentage.values()
        )

        if total_percentage != Decimal("100"):
            raise ValueError("Total percentage must be 100%")

        if any(Decimal(value)<= 0 for value in percentage.values()):
            raise ValueError("Percentage cannot be 0")

        total_paise = int(amount*100)
        split = []
        allocated_paise = 0

        for user in participant:
            user_percentage = Decimal(percentage[user.user_id])

            share_paisa = int(
                (Decimal(total_paise)*user_percentage/Decimal("100"))
                .to_integral_value(rounding= ROUND_DOWN)
            )
            allocated_paise += share_paisa

            split.append([user, share_paisa])
        remaining_paisa = total_paise - allocated_paise

        for index in range(remaining_paisa):
            split[index][1] += 1

        result = []
        for user, share_paisa in split:
            share = Decimal(share_paisa)/Decimal("100")
            result.append(ExpenceSplit(user.name, share))

        return result
         