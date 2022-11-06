class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name) -> None:
        self.WasRun = None
        super().__init__(name)

    def testMethod(self):
        self.WasRun = 1


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert not test.WasRun
        test.run()
        assert test.WasRun


TestCaseTest("testRunning").run()
