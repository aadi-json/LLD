from models.user import User
from decimal import Decimal
from typing import List,Dict
from models.expense_split import ExpenceSplit
from statergies.split_statergy import SplitStatergy


class ExactSplit():
    def split(
            self,
            amount: Decimal,
            participants: List[User],
            exact_share: Dict[int, Decimal]
    ) -> List[ExpenceSplit]:

        if not participants:
            raise ValueError("Participants cannot be empty")

        if amount <= Decimal("0"):
            raise ValueError("amount cannot be zero or less than 0")

        participants_ids = {user.user_id for user in participants}

        print(participants_ids)
        if set(exact_share.keys()) != participants_ids:
            raise ValueError("Share must be provided for every participant")

        total = sum(
            (Decimal(share) for share in exact_share.values()),
            Decimal("0")
        )
        print(total)

        if total != amount:
            raise ValueError("Total share must be equal the expence")

        split = []
        for user in participants:
            share = Decimal(exact_share[user.user_id])
            print(share)
            if share < Decimal("0"):
                raise ValueError("Share cannot be negative")

            split.append(ExpenceSplit(user.name,share))
        return split