import unittest
from test_addition import add

class TestAddition(unittest.TestCase):
  # Define the first unit test
  def test_add(self):
    result = add(3, 4)

    # Define the expected output
    expected_result = 7
    self.assertEqual(result, expected_result)


if __name__ == '__main__':
  unittest.main()