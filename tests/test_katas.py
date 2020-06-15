import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        # self.fail("TODO: Write add unit test")
        self.assertEqual(
            katas.add(2, 3), 5, "Incorrect 2 + 3 is 5")

    def test_multiply(self):
        # self.fail("TODO: Write multiply unit test")
        self.assertEqual(
            katas.multiply(2, 3), 6, "Incorrect 2 * 3 is 6")

    def test_power(self):
        # self.fail("TODO: Write power unit test")
        self.assertEqual(
            katas.power(2, 3), 8, "Incorrect 2^3 is 8")

    def test_factorial(self):
        # self.fail("TODO: Write factorial unit test")
        self.assertEqual(
            katas.factorial(3), 6, "Incorrect 3! is 6")

    def test_fibonacci(self):
        # self.fail("TODO: Write fibonacci unit test")
        self.assertEqual(
            katas.fibonacci(1), 0, "Incorrect first fibonacci number is 1")


if __name__ == '__main__':
    unittest.main()
