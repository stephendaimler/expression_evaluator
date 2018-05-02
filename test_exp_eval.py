import unittest
from exp_eval import exp_eval
import operator

class TestExpressionEvaluator(unittest.TestCase):
    
    def setUp(self):
        self.ops = { "+": operator.add, "-": operator.sub }

    def tearDown(self):
        self.ops = None
    
    def test_plus_one_two(self):
        s = "+ 1 2"
        self.assertEqual(exp_eval(self.ops,s), 3)

    def test_minus_one_two(self):
        s = "- 1 2"
        self.assertEqual(exp_eval(self.ops,s), -1)

    def test_plus_neg_one_neg_two(self):
        s = "+ -1 -2"
        self.assertEqual(exp_eval(self.ops,s), -3)

    def test_plus_one_plus_two_three(self):
        s = "+ 1 + 2 3"
        self.assertEqual(exp_eval(self.ops,s), 6)

    def test_plus_one_plus_two_minus_two_three(self):
        s = "+ 1 + 2 - 2 3"
        self.assertEqual(exp_eval(self.ops,s), 2)

    def test_plus_plus_two_three_two(self):
        s = "+ + 2 3 2"
        self.assertEqual(exp_eval(self.ops,s), 7)

    def test_plus_plus_plus_two_three_two(self):
        s = "+ + + 2 3 2 2"
        self.assertEqual(exp_eval(self.ops,s), 9)

    def test_plus_plus_plus_two_three_two(self):
        s = "+ + + 2 3 2 - 2 3"
        self.assertEqual(exp_eval(self.ops,s), 6)
    
    def test_plus_one_plus_two_minus_three_plus_four_five(self):
        s = "+ 1 + 2 - 3 + 4 5"
        self.assertEqual(exp_eval(self.ops,s), -3)

if __name__ == '__main__':
    unittest.main()