"""
Quick-Calc: A simple calculator application.

This module provides basic arithmetic operations: addition, subtraction,
multiplication, and division with error handling.
"""


class Calculator:
    """A simple calculator for basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator with a result of 0."""
        self.result = 0

    def add(self, a, b):
        """
        Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The sum of a and b
        """
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        """
        Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            The difference (a - b)
        """
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The product of a and b
        """
        self.result = a * b
        return self.result

    def divide(self, a, b):
        """
        Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            The quotient (a / b)

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.result = a / b
        return self.result

    def clear(self):
        """Reset the calculator result to zero."""
        self.result = 0
        return self.result

    def get_result(self):
        """
        Get the current result.

        Returns:
            The current result
        """
        return self.result


class CalculatorUI:
    """User interface for the calculator."""

    def __init__(self):
        """Initialize the calculator UI."""
        self.calculator = Calculator()
        self.display = "0"
        self.pending_operation = None
        self.pending_operand = None
        self.is_new_number = True

    def input_digit(self, digit):
        """
        Input a digit into the calculator.

        Args:
            digit: A single digit (0-9)
        """
        if self.is_new_number:
            self.display = str(digit)
            self.is_new_number = False
        else:
            if self.display == "0":
                self.display = str(digit)
            else:
                self.display += str(digit)

    def input_decimal(self):
        """Input a decimal point."""
        if self.is_new_number:
            self.display = "0."
            self.is_new_number = False
        elif "." not in self.display:
            self.display += "."

    def press_operation(self, operation):
        """
        Press an operation button.

        Args:
            operation: The operation to perform ('+', '-', '*', '/')
        """
        current_value = float(self.display)

        if self.pending_operation is not None:
            # Execute pending operation
            self._execute_pending_operation(current_value)
        else:
            self.pending_operand = current_value

        self.pending_operation = operation
        self.is_new_number = True

    def press_equals(self):
        """Press the equals button to execute the pending operation."""
        if self.pending_operation is None:
            return

        current_value = float(self.display)
        self._execute_pending_operation(current_value)
        self.pending_operation = None
        self.is_new_number = True

    def _execute_pending_operation(self, current_value):
        """Execute the pending operation."""
        if self.pending_operation == "+":
            result = self.calculator.add(self.pending_operand, current_value)
        elif self.pending_operation == "-":
            result = self.calculator.subtract(self.pending_operand, current_value)
        elif self.pending_operation == "*":
            result = self.calculator.multiply(self.pending_operand, current_value)
        elif self.pending_operation == "/":
            try:
                result = self.calculator.divide(self.pending_operand, current_value)
            except ValueError:
                self.display = "Error"
                return
        else:
            return

        # Format result
        if isinstance(result, float) and result == int(result):
            self.display = str(int(result))
        else:
            self.display = str(result)

        self.pending_operand = result

    def press_clear(self):
        """Press the clear button to reset the calculator."""
        self.calculator.clear()
        self.display = "0"
        self.pending_operation = None
        self.pending_operand = None
        self.is_new_number = True

    def get_display(self):
        """
        Get the current display value.

        Returns:
            The string currently displayed on the calculator
        """
        return self.display
