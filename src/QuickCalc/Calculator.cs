using System;

namespace QuickCalcLib
{
    public class Calculator
    {
        public double Add(double a, double b) => a + b;
        public double Subtract(double a, double b) => a - b;
        public double Multiply(double a, double b) => a * b;
        public double Divide(double a, double b)
        {
            if (b == 0) throw new DivideByZeroException("Cannot divide by zero");
            return a / b;
        }
    }

    // A thin input layer to simulate calculator button presses (used by integration tests)
    public class CalculatorState
    {
        private readonly Calculator _calc = new Calculator();
        private double _left = 0;
        private string? _op = null;
        private bool _entering = false;

        public string Display { get; private set; } = "0";

        public void EnterNumber(string digits)
        {
            if (!_entering || Display == "0") Display = digits;
            else Display += digits;
            _entering = true;
        }

        public void PressOperator(string op)
        {
            if (_entering)
            {
                if (double.TryParse(Display, out var val)) _left = val;
                _entering = false;
            }
            _op = op;
            Display = "0";
        }

        public void PressEquals()
        {
            try
            {
                if (!double.TryParse(Display, out var right)) right = 0;
                double result = _op switch
                {
                    "+" => _calc.Add(_left, right),
                    "-" => _calc.Subtract(_left, right),
                    "*" or "×" => _calc.Multiply(_left, right),
                    "/" or "÷" => _calc.Divide(_left, right),
                    _ => right
                };

                Display = result.ToString();
                _left = result;
                _op = null;
                _entering = false;
            }
            catch (DivideByZeroException)
            {
                Display = "Error";
                _left = 0;
                _op = null;
                _entering = false;
            }
        }

        public void PressClear()
        {
            _left = 0;
            _op = null;
            _entering = false;
            Display = "0";
        }
    }
}
