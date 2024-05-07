import unittest
import sys
from time import time

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFact(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.start = time()

    @classmethod
    def tearDownClass(cls):
        cls.end = time()

        print(f"\nВремя выполнения тестов {cls.end - cls.start:.6f} секунд")

    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)
    
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_almost_big(self):
        self.assertEqual(factorial(20), 2432902008176640000)

    def test_large(self):
        with self.assertRaises(ValueError):
            factorial(21)

if __name__ == "__main__":
    unittest.main()