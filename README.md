# Quick-Calc (C#)

Quick-Calc is a minimal calculator application implemented in C#. It provides basic arithmetic operations (addition, subtraction, multiplication, division) and a small input layer that simulates calculator button presses. The project focuses on clean design and a multi-layered test suite (unit + integration).

## Project Layout

- `src/QuickCalc/` — Calculator library and console front-end
- `tests/QuickCalc.Tests/` — Unit and integration tests using xUnit

## Requirements implemented

- Addition, subtraction, multiplication, division
- Division-by-zero is handled gracefully by the input layer (display shows `Error`)
- Clear (C) resets the state/display to `0`

## Setup

Prerequisites: .NET SDK (6.0 or later recommended)

Restore and build:

```bash
dotnet restore
dotnet build
```

Run the console app (optional):

```bash
cd src/QuickCalc
dotnet run
```

## Running tests

From repository root run:

```bash
dotnet test
```

All tests are written with xUnit. See `TESTING.md` for discussion of the testing strategy.

## Testing Framework Research

xUnit vs NUnit

xUnit is a modern test framework that emphasizes test isolation and supports parallel test execution out of the box. It integrates well with .NET Core and the `dotnet test` workflow. Tests are written with attributes like `[Fact]` and `[Theory]`.

NUnit is a long-standing, feature-rich framework with broad community support and many assertion helpers. NUnit's attribute model is similar to many developers' expectations and it has mature tooling.

Choice justification: For this assignment I chose xUnit because of its lean integration with `dotnet test`, the simplicity of test discovery, and strong support for modern .NET Core workflows.


## Release

After verifying tests and features, create a GitHub Release and tag `v1.0.0` with a short release note describing the implemented features and tests.
