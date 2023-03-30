import unittest

from controller.calculator import DemoController

class TestDemoCalculator(unittest.TestCase):

    def test_valid_user_password(self):
        print('test_valid_user_password')

    def test_invalid_user_password(self):
        print('test_invalid_user_password')

    def test_valid_addition(self):
        print('test_valid_addition')

    def test_invalid_addition(self):
        dobj = DemoController()
        result = dobj.addition(-1002,-355)
        self.assertEqual(result,"Only +ve numbers are required")
        print('test_invalid_addition')

    def test_demo(self):
        print('demo test')


if __name__ == '__main__':
    unittest.main()
