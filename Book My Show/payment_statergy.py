from abc import ABC, abstractmethod

class PaymentStatergy(ABC):
    @abstractmethod
    def pay(self, amount:float):
        pass

class UPI(PaymentStatergy):
    def pay(self, amount):
        print(f"Payment of Rs. {amount} successful using UPI")
        return True

class Card(PaymentStatergy):
    def pay(self, amount):
        print(f"Payment of Rs. {amount} successful using Card")
        return True