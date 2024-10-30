import unittest
from math_quiz import create_random_integer, select_random_mathoperator, create_problem_and_answer


class TestMathGame(unittest.TestCase):

    def test_create_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = create_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_select_random_mathoperator(self):
        # Test if the selected operator is one of '+', '-', '*'
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random operators
            mathoperator = select_random_mathoperator()
            self.assertIn(mathoperator, valid_operators)

    def test_create_problem_and_answer(self):
        # Define test cases (number_1, number_2, mathoperator, expected_problem, expected_answer)    
        test_cases = [
            # Operations with positive numbers
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),

            # Operations with zero
            (0, 0, '+', '0 + 0', 0),
            (0, 5, '-', '0 - 5', -5),
            (5, 0, '*', '5 * 0', 0),

            # Operations with negative numbers
            (-5, 3, '+', '-5 + 3', -2),
            (5, -3, '-', '5 - -3', 8),
            (-5, -3, '*', '-5 * -3', 15),

        ]

        for number_1, number_2, mathoperator, expected_problem, expected_answer in test_cases:
            problem, answer = create_problem_and_answer(number_1, number_2, mathoperator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
