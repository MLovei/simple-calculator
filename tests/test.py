import unittest
from calculator import Calculator
from hypothesis import given, assume, strategies as st


class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Initialize the calculator for each test
        self.calculator = Calculator()

    def test_addition(self):
        """Test that it can add 2 values"""
        self.assertEqual(self.calculator.add(2), 2.0)
        # Testing if the same works with float values
        self.calculator.add(10)
        self.assertEqual(self.calculator.add(2.0), 14.0)

    def test_subtraction(self):
        """Test that it can subtract 2 values"""
        self.assertEqual(self.calculator.sub(2), -2.0)
        # Testing if the same works with float values
        self.calculator.add(10)
        self.assertEqual(self.calculator.sub(2.0), 6.0)

    def test_multiplication(self):
        """Test that it can multiplicate 2 values"""
        self.calculator.add(11)
        
        self.assertEqual(self.calculator.mult(3), 33.0)
        # Testing if the same works with float values
        self.calculator.add(11.0)
        self.assertEqual(self.calculator.mult(2.0), 88.0)

    def test_division(self):
        """Test that it can divide 2 values"""
        self.calculator.add(5)
        self.assertEqual(self.calculator.div(8), 0.625)
        # Testing if the same works with float values
        self.calculator.add(3.375)
        self.assertEqual(self.calculator.div(2), 2.0)

    def test_root1(self):
        """Test that it can take square root of a value"""
        self.calculator.add(25)
        self.assertEqual(self.calculator.root(2), 5.0)

    def test_root2(self):
        """Test that it can take cubic root of a value"""
        self.calculator.add(125)
        self.assertEqual(self.calculator.root(3), 5.0)
        # Testing if the same works with float values
        self.calculator.add(120.0)
        self.assertEqual(self.calculator.root(3), 5.0)

    def test_reset(self):
        """Test that it can reset the value to 0"""
        self.calculator.add(25)
        self.calculator.add(25.5)
        self.assertEqual(self.calculator.reset(), 0.0)

    def test_chain(self):
        """Test if the memory variable updates after multiple operations"""
        self.assertEqual(self.calculator.add(2), 2.0)
        self.assertEqual(self.calculator.sub(1), 1.0)
        self.assertEqual(self.calculator.mult(72), 72.0)
        self.assertEqual(self.calculator.div(9), 8.0)
        self.assertEqual(self.calculator.root(3), 2.0)
        self.assertEqual(self.calculator.reset(), 0.0)

    @given(
        st.floats(min_value=0, max_value=99999.9999999999),
        st.floats(min_value=-99999.9999999999, max_value=0),
    )
    def test_add_hypo(self, positive_numbers, negative_numbers):
        # We test the add() function with positive and negative value range
        positives = Calculator()
        negatives = Calculator()
        assert positives.add(positive_numbers) >= 0
        assert negatives.add(negative_numbers) <= 0

    @given(
        st.floats(min_value=0, max_value=99999.9999999999),
        st.floats(min_value=-99999.9999999999, max_value=0),
    )
    def test_sub_hypo(self, positive_numbers, negative_numbers):
        # We test the sub() function with positive and negative value range
        positives = Calculator()
        negatives = Calculator()
        assert positives.sub(positive_numbers) <= 0
        assert negatives.sub(negative_numbers) >= 0

    @given(st.floats())
    def test_mult_hypo(self, range):
        # We test the mult() function with positive and negative value range
        numbers = Calculator(0, 1)  # Memory set to 1 so we dont get 0 always
        assert numbers.mult(range) != ZeroDivisionError
        assert numbers.mult(range) != ValueError

    @given(st.floats())
    def test_div_hypo(self, range):
        # We test the div() function with positive & negative float value range
        assume(range != 0)  # excluding division by 0
        numbers = Calculator(0, 1)
        assert numbers.div(range) != ZeroDivisionError
        assert numbers.div(range) != ValueError

    @given(st.integers(min_value=-10, max_value=10))
    def test_root_hypo(self, range):
        # We test the root() function with positive & negative int value range
        assume(range != 0)  # excluding division by 0
        numbers = Calculator(0, 1)
        assert numbers.root(range) != ValueError


if __name__ == "__main__":
    unittest.main()
