class Money:
    def __eq__(self, __o):
        return __o.amount == self.amount

    def equals(self, money):
        return self.amount == money.amount


class Dollar(Money):
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(Money):
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
