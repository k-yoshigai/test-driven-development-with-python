class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, __o):
        return __o.amount == self.amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, dollar):
        return self.amount == dollar.amount


class Franc:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, __o):
        return __o.amount == self.amount

    def times(self, multiplier):
        return Franc(self.amount * multiplier)

    def equals(self, dollar):
        return self.amount == dollar.amount
