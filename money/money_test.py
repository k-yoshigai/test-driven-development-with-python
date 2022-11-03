import money


class TestMoney:
    def test_multiplication(self):
        five = money.Dollar(5)
        assert money.Dollar(10) == five.times(2)
        assert money.Dollar(15) == five.times(3)

        five = money.Franc(5)
        assert money.Franc(10) == five.times(2)
        assert money.Franc(15) == five.times(3)

    def test_equality(self):
        assert money.Dollar(5).equals(money.Dollar(5))
        assert not money.Dollar(5).equals(money.Dollar(6))

        assert money.Franc(5).equals(money.Franc(5))
        assert not money.Franc(5).equals(money.Franc(6))
