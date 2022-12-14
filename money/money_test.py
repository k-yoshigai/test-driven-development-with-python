import money


class TestMoney:
    def test_multiplication(self):
        five = money.Money.dollar(5)
        assert money.Money.dollar(10) == five.times(2)
        assert money.Money.dollar(15) == five.times(3)

        five = money.Money.franc(5)
        assert money.Money.franc(10) == five.times(2)
        assert money.Money.franc(15) == five.times(3)

    def test_equality(self):
        assert money.Money.dollar(5).equals(money.Money.dollar(5))
        assert not money.Money.dollar(5).equals(money.Money.dollar(6))

        assert money.Money.franc(5).equals(money.Money.franc(5))
        assert not money.Money.franc(5).equals(money.Money.franc(6))

        assert not money.Money.dollar(5).equals(money.Money.franc(5))

    def test_simple_addition(self):
        five = money.Money.dollar(5)
        sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum, "USD")
        assert money.dollar(10) == reduced
