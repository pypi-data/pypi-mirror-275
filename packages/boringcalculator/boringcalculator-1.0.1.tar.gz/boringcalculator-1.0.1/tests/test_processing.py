import unittest

from boringcalculator import OperationProcessor


class TestOperationProcessor(unittest.TestCase):
    def test_graph(self):
        # Test case 1: Test graphing a valid function
        operation = "x**2"
        processor = OperationProcessor(operation)
        image = processor.graph()
        self.assertIsNotNone(image)

        # Test case 2: Test graphing an invalid function
        operation = "1 / x"
        processor = OperationProcessor(operation)
        image = processor.graph()
        self.assertIsNotNone(image)

    def test_integrate(self):
        # Test case 1: Test integrating a valid function
        operation = "x**2"
        processor = OperationProcessor(operation)
        integral = processor.integrate()
        self.assertEqual(
            integral, r"\(\displaystyle \int x^{2}\, dx = \frac{x^{3}}{3}+C\)"
        )

        # Test case 2: Test integrating an invalid function
        operation = "1 / x"
        processor = OperationProcessor(operation)
        integral = processor.integrate()
        self.assertEqual(integral, "Could not solve this integral")


if __name__ == "__main__":
    unittest.main()
