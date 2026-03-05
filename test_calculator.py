"""
Unit and Integration Tests for Quick-Calc.

This module contains comprehensive tests for the calculator application,
including unit tests for individual operations and integration tests
for complete user interactions.
"""

import pytest
from calculator import Calculator, CalculatorUI


# ============================================================================
# UNIT TESTS
# ============================================================================


class TestCalculatorAddition:
    """Unit tests for addition operation."""

    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        calc = Calculator()
        result = calc.add(5, 3)
        assert result == 8

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        calc = Calculator()
        result = calc.add(-5, -3)
        assert result == -8


class TestCalculatorSubtraction:
    """Unit tests for subtraction operation."""

    def test_subtract_positive_numbers(self):
        """Test subtraction of two positive numbers."""
        calc = Calculator()
        result = calc.subtract(10, 4)
        assert result == 6

    def test_subtract_resulting_in_negative(self):
        """Test subtraction resulting in a negative number."""
        calc = Calculator()
        result = calc.subtract(3, 10)
        assert result == -7


class TestCalculatorMultiplication:
    """Unit tests for multiplication operation."""

    def test_multiply_positive_numbers(self):
        """Test multiplication of two positive numbers."""
        calc = Calculator()
        result = calc.multiply(6, 7)
        assert result == 42

    def test_multiply_with_zero(self):
        """Test multiplication by zero."""
        calc = Calculator()
        result = calc.multiply(100, 0)
        assert result == 0


class TestCalculatorDivision:
    """Unit tests for division operation."""

    def test_divide_positive_numbers(self):
        """Test division of two positive numbers."""
        calc = Calculator()
        result = calc.divide(10, 2)
        assert result == 5

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_divide_decimal_result(self):
        """Test division resulting in decimal."""
        calc = Calculator()
        result = calc.divide(7, 2)
        assert result == 3.5

    def test_divide_large_numbers(self):
        """Test division with large numbers."""
        calc = Calculator()
        result = calc.divide(1000000, 1000)
        assert result == 1000


class TestCalculatorEdgeCases:
    """Unit tests for edge cases and special scenarios."""

    def test_clear_resets_result(self):
        """Test that clear resets the result to zero."""
        calc = Calculator()
        calc.add(5, 3)
        calc.clear()
        assert calc.get_result() == 0

    def test_result_persistence(self):
        """Test that results are stored for chaining operations."""
        calc = Calculator()
        calc.add(5, 3)
        assert calc.get_result() == 8
        result2 = calc.add(8, 2)
        assert result2 == 10


# ============================================================================
# INTEGRATION TESTS
# ============================================================================


class TestCalculatorUIIntegration:
    """Integration tests for calculator UI and logic together."""

    def test_full_calculation_addition(self):
        """
        Integration test: Full user interaction.
        Simulate: 5 + 3 = 8
        """
        ui = CalculatorUI()
        ui.input_digit(5)
        assert ui.get_display() == "5"

        ui.press_operation("+")
        assert ui.pending_operation == "+"

        ui.input_digit(3)
        assert ui.get_display() == "3"

        ui.press_equals()
        assert ui.get_display() == "8"

    def test_full_calculation_sequence_with_clear(self):
        """
        Integration test: Complete calculation with clear.
        Perform: 5 + 3 = 8, then clear, then 10 - 4 = 6
        """
        ui = CalculatorUI()

        # First calculation: 5 + 3 = 8
        ui.input_digit(5)
        ui.press_operation("+")
        ui.input_digit(3)
        ui.press_equals()
        assert ui.get_display() == "8"

        # Clear
        ui.press_clear()
        assert ui.get_display() == "0"
        assert ui.pending_operation is None

        # Second calculation: 10 - 4 = 6
        ui.input_digit(1)
        ui.input_digit(0)
        ui.press_operation("-")
        ui.input_digit(4)
        ui.press_equals()
        assert ui.get_display() == "6"

    def test_chained_operations(self):
        """
        Integration test: Chained operations.
        Calculate: 5 + 3 - 2 = 6
        """
        ui = CalculatorUI()
        ui.input_digit(5)
        ui.press_operation("+")
        ui.input_digit(3)
        ui.press_operation("-")  # Should execute 5+3=8, then prepare 8-...
        assert ui.get_display() == "8"

        ui.input_digit(2)
        ui.press_equals()
        assert ui.get_display() == "6"

    def test_division_by_zero_in_ui(self):
        """Integration test: Division by zero is handled gracefully in UI."""
        ui = CalculatorUI()
        ui.input_digit(1)
        ui.input_digit(0)
        ui.press_operation("/")
        ui.input_digit(0)
        ui.press_equals()
        assert ui.get_display() == "Error"

    def test_multiplication_then_subtraction(self):
        """
        Integration test: Multiple operations.
        Calculate: 6 * 7 - 12 = 30
        """
        ui = CalculatorUI()
        ui.input_digit(6)
        ui.press_operation("*")
        ui.input_digit(7)
        ui.press_operation("-")  # Should execute 6*7=42, then prepare 42-...
        assert ui.get_display() == "42"

        ui.input_digit(1)
        ui.input_digit(2)
        ui.press_equals()
        assert ui.get_display() == "30"

    def test_decimal_input_and_calculation(self):
        """Integration test: Decimal number input and calculation."""
        ui = CalculatorUI()
        ui.input_digit(5)
        ui.input_decimal()
        ui.input_digit(5)
        ui.press_operation("+")
        ui.input_digit(2)
        ui.press_equals()
        assert ui.get_display() == "7.5"
