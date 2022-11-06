class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, __o):
        is_same_class_name = self.__class__.__name__ == __o.__class__.__name__
        return __o.amount == self.amount and is_same_class_name

    def equals(self, money):
        is_same_currency = self.currency == money.currency
        return self.amount == money.amount and is_same_currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")
