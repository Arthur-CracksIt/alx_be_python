import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self): #testing_addition
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self): #testing_subtraction
        self.assertEqual(self.calc.subtract(2,3), -1)
        self.assertEqual(self.calc.subtract(4,0), 4)
        self.assertEqual(self.calc.subtract(5,2), 3)
        self.assertEqual(self.calc.subtract(0,0), 0)

    def test_multiplication(self): #testing multiplication
        self.assertEqual(self.calc.multiply(2,4), 8)
        self.assertEqual(self.calc.multiply(-1,4), -4)
        self.assertEqual(self.calc.multiply(-1,-10), 10)
        self.assertEqual(self.calc.multiply(0,0), 0)
    
    def test_division(self): #testing division
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assertEqual(self.calc.divide(0, 4), 0)
        self.assertEqual(self.calc.divide(5, -1), -5)
        self.assertEqual(self.calc.divide(4, 0), 0)
        

if __name__ == "__main__":
    unittest.main()

