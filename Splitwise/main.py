from models.user import User
from models.group import Group
from models.expence import Expence
from decimal import Decimal
from models.expense_split import ExpenceSplit
from statergies.equal_split import EqualSplit
from statergies.exact_split import ExactSplit


user_1 = User("Aditya@123", "aditya@gmail.com", "Aditya Gawande")
user_2 = User("Shasta@123", "shasta@gmail.com", "Shasta Tyade")
# print(user_1)
# print(user_2)

# print("------group--------")
# group = Group(101, "Goa Trip")
# group.add_member(user_1)
# group.add_member(user_2)
# group.get_members()

# print("-------Expence------")
# expence = Expence(1, "Dinner", Decimal("1200"),user_1, group)
# print(expence.get_details())

# print("----- Split Expence ------")
# split_expence = ExpenceSplit(user_1, Decimal("500"))
# print(split_expence.get_details())

# print("------ Equal Split ---------")
# participants = [user_1.name, user_2.name]

# equal_split = EqualSplit()

# splits = equal_split.split(Decimal("1200"), participants)

# for split in splits:
#     print(split.get_details())


participants = [user_1, user_2]

exact_shares = {
    user_1.user_id: Decimal("700"),
    user_2.user_id: Decimal("500")
}

exact_split = ExactSplit()

splits = exact_split.split(
    Decimal("1200"),
    participants,
    exact_shares
)

print("------ Exact Split ---------")

for split in splits:
    print(split.get_details())