class Money:
    def __eq__(self, __o):
        is_same_class_name = self.__class__.__name__ == __o.__class__.__name__
        return __o.amount == self.amount and is_same_class_name

    def equals(self, money):
        is_same_class_name = self.__class__.__name__ == money.__class__.__name__
        return self.amount == money.amount and is_same_class_name

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)


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
