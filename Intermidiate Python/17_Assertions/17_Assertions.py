import unittest
import test_class

class TestStringUtil(unittest.TestCase):
    def test_reverse_string(self):
        reverse_string = test_class.reverse_string
        self.assertEqual(reverse_string("Hello"), "olleH")
        self.assertEqual(reverse_string(" "), " ")
        self.assertEqual(reverse_string("bA"), "Ab")
        self.assertNotEqual(reverse_string(" "), "hello")

    def test_capitalize_string(self):
        capitalize_string = test_class.capitalize_string
        self.assertEqual(capitalize_string("hello"), "Hello")
        self.assertEqual(capitalize_string(" "), " ")
        self.assertNotEqual(capitalize_string("Hello"), "hello")

    def is_capitalize_string(self, string):
        capitalize_string = test_class.is_capitalize_string
        self.assertEqual(capitalize_string("Hello"), "Hello")
        self.assertNotEqual(capitalize_string(" "), "hello")
        self.assertNotEqual(capitalize_string("hello"), "Hello")




if __name__ == '__main__':
    unittest.main()