import unittest
from boolgen import parse_input, simplify_expression

class TestBoolgen(unittest.TestCase):

    def test_parse_input_single_output(self):
        input_data = """A B C D=
                        0 0 0 0
                        0 0 1 1
                        0 1 0 1
                        0 1 1 0
                        1 0 0 1
                        1 0 1 0
                        1 1 0 0
                        1 1 1 1"""
        input_vars, output_vars, truth_table = parse_input(input_data)
        expected_input_vars = ['A', 'B', 'C']
        expected_output_vars = ['D']
        expected_truth_table = [
            [0, 0, 0, 0],
            [0, 0, 1, 1],
            [0, 1, 0, 1],
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 0],
            [1, 1, 1, 1]
        ]
        self.assertEqual(input_vars, expected_input_vars)
        self.assertEqual(output_vars, expected_output_vars)
        self.assertEqual(truth_table, expected_truth_table)

    def test_parse_input_implicit_output(self):
        input_data = """A B
                        0 0
                        0 1
                        1 0
                        1 1"""
        input_vars, output_vars, _ = parse_input(input_data)
        expected_input_vars = ['A']
        expected_output_vars = ['B']
        self.assertEqual(input_vars, expected_input_vars)
        self.assertEqual(output_vars, expected_output_vars)

    def test_parse_input_multiple_outputs(self):
        input_data = """A B C D= E=
                        0 0 0 0 1
                        0 0 1 1 0
                        0 1 0 1 0
                        0 1 1 0 1
                        1 0 0 1 0
                        1 0 1 0 1
                        1 1 0 0 1
                        1 1 1 1 0"""
        input_vars, output_vars, truth_table = parse_input(input_data)
        expected_input_vars = ['A', 'B', 'C']
        expected_output_vars = ['D', 'E']
        expected_truth_table = [
            [0, 0, 0, 0, 1],
            [0, 0, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1],
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [1, 1, 0, 0, 1],
            [1, 1, 1, 1, 0]
        ]
        self.assertEqual(input_vars, expected_input_vars)
        self.assertEqual(output_vars, expected_output_vars)
        self.assertEqual(truth_table, expected_truth_table)

    def test_simplify_expression_single_output(self):
        input_data = """A B C D=
                        0 0 0 0
                        0 0 1 1
                        0 1 0 1
                        0 1 1 0
                        1 0 0 1
                        1 0 1 0
                        1 1 0 0
                        1 1 1 1"""
        input_vars, output_vars, truth_table = parse_input(input_data)
        expression = simplify_expression(input_vars, truth_table, 0)
        expected_expression = "A & B & C | A & ~B & ~C | B & ~A & ~C | C & ~A & ~B"
        sorted_expected_expression = ' | '.join(sorted(expected_expression.split(' | ')))

        self.assertEqual(expression, sorted_expected_expression)

    def test_simplify_expression_multiple_outputs(self):
        input_data = """A B C D= E=
                        0 0 0 0 1
                        0 0 1 1 0
                        0 1 0 1 0
                        0 1 1 0 1
                        1 0 0 1 0
                        1 0 1 0 1
                        1 1 0 0 1
                        1 1 1 1 0"""
        input_vars, output_vars, truth_table = parse_input(input_data)
        expression1 = simplify_expression(input_vars, truth_table, 0)
        expression2 = simplify_expression(input_vars, truth_table, 1)

        expected_expression1 = "A & B & C | A & ~B & ~C | B & ~A & ~C | C & ~A & ~B"
        expected_expression2 = "A & B & ~C | A & C & ~B | B & C & ~A | ~A & ~B & ~C"
        sorted_expected_expression1 = ' | '.join(sorted(expected_expression1.split(' | ')))
        sorted_expected_expression2 = ' | '.join(sorted(expected_expression2.split(' | ')))

        self.assertEqual(expression1, sorted_expected_expression1)
        self.assertEqual(expression2, sorted_expected_expression2)

    def test_simplify_expression_all_zeros(self):
        input_data = """A B C D=
                        0 0 0 0
                        0 0 1 0
                        0 1 0 0
                        0 1 1 0
                        1 0 0 0
                        1 0 1 0
                        1 1 0 0
                        1 1 1 0"""
        input_vars, output_vars, truth_table = parse_input(input_data)
        expression = simplify_expression(input_vars, truth_table, 0)
        expected_expression = "0"

        self.assertEqual(expression, expected_expression)

    def test_simplify_expression_all_ones(self):
        input_data = """A B C D=
                        0 0 0 1
                        0 0 1 1
                        0 1 0 1
                        0 1 1 1
                        1 0 0 1
                        1 0 1 1
                        1 1 0 1
                        1 1 1 1"""
        input_vars, output_vars, truth_table = parse_input(input_data)
        expression = simplify_expression(input_vars, truth_table, 0)
        expected_expression = "1"

        self.assertEqual(expression, expected_expression)

    def test_simplify_expression_some_simplification(self):
        input_data = """A B C D=
                        0 0 0 0
                        0 0 1 1
                        0 1 0 1
                        0 1 1 1
                        1 0 0 0
                        1 0 1 1
                        1 1 0 1
                        1 1 1 1"""
        input_vars, output_vars, truth_table = parse_input(input_data)
        expression = simplify_expression(input_vars, truth_table, 0)
        expected_expression = "B | C"

        self.assertEqual(expression, expected_expression)

if __name__ == '__main__':
    unittest.main()
