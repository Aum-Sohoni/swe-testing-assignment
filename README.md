# Quick-Calc: A Professional Calculator Application

## Project Description

Quick-Calc is a simple yet fully-featured calculator application implementing core arithmetic operations. The project demonstrates professional software development practices including comprehensive testing, meaningful version control, and thorough documentation. The application supports addition, subtraction, multiplication, division, and clear operations with proper error handling for edge cases like division by zero.

This project serves as a practical implementation of software testing principles covered in Lecture 3, including unit testing, integration testing, and the testing pyramid methodology.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, and division
- **Error Handling**: Graceful handling of division by zero
- **Clear Function**: Reset calculator state
- **Decimal Support**: Handle decimal numbers in calculations
- **Chained Operations**: Support for consecutive operations (e.g., 5 + 3 - 2)
- **Comprehensive Testing**: Full unit and integration test coverage

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/swe-testing-assignment.git
   cd swe-testing-assignment
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Usage

### As a Library

```python
from calculator import Calculator

# Create a calculator instance
calc = Calculator()

# Perform operations
result = calc.add(5, 3)        # Returns 8
result = calc.subtract(10, 4)  # Returns 6
result = calc.multiply(6, 7)   # Returns 42
result = calc.divide(10, 2)    # Returns 5

# Clear the calculator
calc.clear()
```

### Using the UI

```python
from calculator import CalculatorUI

# Create a UI instance
ui = CalculatorUI()

# Simulate user input: 5 + 3 = 8
ui.input_digit(5)
ui.press_operation("+")
ui.input_digit(3)
ui.press_equals()
print(ui.get_display())  # Output: "8"

# Clear the calculator
ui.press_clear()
```

## Running Tests

All unit and integration tests can be executed with a single command:

```bash
pytest test_calculator.py -v
```

### Additional Testing Options

Run tests with coverage report:
```bash
pytest test_calculator.py --cov=calculator --cov-report=html
```

Run specific test class:
```bash
pytest test_calculator.py::TestCalculatorAddition -v
```

Run with detailed output:
```bash
pytest test_calculator.py -vv
```

## Test Suite Overview

The test suite contains **15 comprehensive tests**:

- **8 Unit Tests**:
  - Addition tests (positive and negative numbers)
  - Subtraction tests
  - Multiplication tests (including zero)
  - Division tests (normal division, division by zero error, decimals, large numbers)
  - Edge cases (clear function, result persistence)

- **7 Integration Tests**:
  - Full calculation workflows
  - Calculation with clear operation
  - Chained operations
  - Division by zero handling in UI
  - Multiple operation sequences
  - Decimal input and calculation

## Testing Framework Research

### Pytest vs Unittest

We chose **Pytest** as our testing framework. Here's our comparative analysis:

#### Pytest

**Advantages**:
- Simple, readable syntax using plain Python assertions (`assert x == y`) instead of special assertion methods
- Powerful fixture system for test setup and teardown
- Excellent plugin ecosystem (pytest-cov for coverage, pytest-xdist for parallel execution)
- Better error messages and stack traces
- Supports parametrized testing for multiple test scenarios
- Can run tests written in unittest format as well
- Less boilerplate code required

**Disadvantages**:
- Requires separate installation (not in standard library)
- Less integrated with IDEs compared to unittest
- Can have a slight learning curve for advanced features

#### Unittest

**Advantages**:
- Part of Python standard library - no installation needed
- Object-oriented approach familiar to Java/C# developers
- Well-established and used in many legacy projects
- Good integration with most Python IDEs

**Disadvantages**:
- Verbose syntax with `self.assertEqual()`, `self.assertTrue()`, etc.
- More boilerplate code required (class structure for each test)
- Less readable assertions make errors harder to diagnose
- Limited plugin ecosystem
- Fixture setup/teardown is less elegant than pytest fixtures

#### Our Choice: Pytest

We selected Pytest because:
1. **Readability**: Plain assertions are easier to understand and maintain
2. **Scalability**: The fixture system scales better as test suite grows
3. **Industry Standard**: Pytest has become the de facto standard in Python development
4. **Developer Experience**: Better error messages and faster development cycle
5. **Coverage Integration**: pytest-cov provides excellent coverage reports

## Project Structure

```
swe-testing-assignment/
├── calculator.py           # Main calculator logic (Calculator and CalculatorUI classes)
├── test_calculator.py      # Unit and integration tests
├── README.md              # This file
├── TESTING.md             # Testing strategy and methodology documentation
├── requirements.txt       # Runtime dependencies
├── requirements-dev.txt   # Development dependencies
└── .gitignore            # Git ignore file
```

## Version History

### v1.0.0 (Current Release)

- Initial release with full calculator functionality
- Complete unit and integration test coverage
- Professional documentation and testing strategy
- Comprehensive error handling and edge case management

## Contributing

This is an assignment submission. However, the code follows professional standards suitable for open-source contributions:
- Clear, documented code with docstrings
- Comprehensive test coverage
- Meaningful commit messages
- Professional documentation

## License

This project is provided as-is for educational purposes.

## Author

Created as part of SWE Testing Assignment - Lecture 3 Practical

## Additional Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Python Testing Best Practices](https://docs.python-guide.org/writing/tests/)
- [Testing Pyramid Concept](https://martinfowler.com/bliki/TestPyramid.html)

---

For detailed testing methodology and strategy, see [TESTING.md](TESTING.md).