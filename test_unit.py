""" test_unit.py """

import unittest

from script import add


class TestAdd(unittest.TestCase):
    """ Test class """
    def setUp(self) -> None:
        pass

    def test_add(self):
        """
            Test for Adding 2 numbers
        """
        num1 = 8
        num2 = 2
        result = add(num1, num2)
        self.assertEqual(result, 10)

if __name__ == "__main__":
    unittest.main()
