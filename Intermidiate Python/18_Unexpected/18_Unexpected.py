import unittest
import test_class

class TestUnexpected(unittest.TestCase):
    def test_get_sqrt(self):
        get_sqrt = test_class.get_sqrt
        self.assertEqual(get_sqrt(144), 12)
        self.assertNotEqual(get_sqrt(144), 0)
        with self.assertRaises(ValueError):
            self.assertEqual(get_sqrt(-1), -1)

    def test_divide(self):
        divide = test_class.divide
        self.assertEqual(divide(4, 2), 2)
        self.assertNotEqual(divide(4, 2), 0)
        with self.assertRaises(ZeroDivisionError):
            # how to test using the first method
            self.assertEqual(divide(4, 0), 0)
            # how to test using the second method
            divide(4, 0)
