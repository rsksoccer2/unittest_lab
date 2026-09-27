import unittest
from my_calculator import add

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

"""
TEST RESULTS EXPLANATION:

I created my_calculator file for Testing of Code
I created test_my_calculator file for Execution of Code
Afterwhich, I ran python test_my_calculator.py -v

Result:
test_add_negative_numbers ... ok
test_add_positive_numbers ... ok
test_add_zero ... ok
Ran 3 tests in 0.002s
OK

Meaning:
- 3 tests means 3 methods starting with test_ were found and run.
- 'ok' and dots mean each test passed - add() returned the expected value.
- 'Ran 3 tests in 0.002s' is the total time taken.
- 'OK' means all assertions were true. self.assertEqual checks if add(a,b) equals expected.
- If a test fails, it would show FAIL instead of ok, with expected vs actual.
- The test runner unittest.main() is what runs the tests and prints the report. 
- Thank you.
"""