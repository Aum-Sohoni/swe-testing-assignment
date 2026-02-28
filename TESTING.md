# TESTING.md

## Testing Strategy

This project uses a layered testing approach following the Testing Pyramid: a broad base of fast unit tests verifying individual methods in `Calculator`, and a smaller number of integration tests that verify interaction between the input layer (`CalculatorState`) and the calculation logic.

What I tested:
- Unit tests: arithmetic operations (add, subtract, multiply, divide), and edge cases such as division by zero, negative numbers, decimal numbers, and very large numbers.
- Integration tests: full user flows (enter digits, choose operator, equals) and UI-like behaviors (Clear, handling division by zero) using the `CalculatorState` input layer.

What I did not test:
- No end-to-end GUI testing because the UI is minimal and out of scope for this assignment.
- No performance or load/non-functional tests; not necessary for a basic calculator.

## Lecture Concepts Mapping

- Testing Pyramid: The suite contains many unit tests (fast, isolated) and fewer integration tests. This reflects the pyramid: unit tests at the base, integration tests in the middle.

- Black-box vs White-box Testing: Unit tests are white-box because they test internal methods directly (`Calculator`). Integration tests are black-box from the perspective of the input layer (`CalculatorState`) because they simulate user interactions without inspecting internals.

- Functional vs Non-Functional Testing: The suite focuses on functional tests (correctness of arithmetic operations and flows). Non-functional aspects (performance, security, usability) were intentionally not tested.

- Regression Testing: The test suite can be run with `dotnet test` in CI. Any future change that breaks arithmetic correctness or user flows will cause tests to fail, catching regressions early.

## Test Results Summary

| Test Name | Type | Status |
|---|---:|---:|
| Add_TwoIntegers_ReturnsSum | Unit | pass |
| Subtract_TwoIntegers_ReturnsDifference | Unit | pass |
| Multiply_TwoIntegers_ReturnsProduct | Unit | pass |
| Divide_TwoIntegers_ReturnsQuotient | Unit | pass |
| Divide_ByZero_ThrowsDivideByZeroException | Unit | pass |
| Operations_WithNegativeNumbers_Works | Unit | pass |
| Operations_WithDecimals_Works | Unit | pass |
| Operations_WithLargeNumbers_Works | Unit | pass |
| FullUserFlow_Addition_ShowsCorrectResult | Integration | pass |
| ClearAfterCalculation_ResetsDisplay | Integration | pass |
| DivideByZero_FromState_ShowsError | Integration | pass |

> Note: Status values above assume tests pass locally; run `dotnet test` to execute and verify on your environment.
