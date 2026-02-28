using Xunit;
using QuickCalcLib;
using System;

namespace QuickCalc.Tests
{
    public class CalculatorUnitTests
    {
        private readonly Calculator _calc = new Calculator();

        [Fact]
        public void Add_TwoIntegers_ReturnsSum()
        {
            Assert.Equal(8, _calc.Add(5, 3));
        }

        [Fact]
        public void Subtract_TwoIntegers_ReturnsDifference()
        {
            Assert.Equal(6, _calc.Subtract(10, 4));
        }

        [Fact]
        public void Multiply_TwoIntegers_ReturnsProduct()
        {
            Assert.Equal(42, _calc.Multiply(6, 7));
        }

        [Fact]
        public void Divide_TwoIntegers_ReturnsQuotient()
        {
            Assert.Equal(2, _calc.Divide(6, 3));
        }

        [Fact]
        public void Divide_ByZero_ThrowsDivideByZeroException()
        {
            Assert.Throws<DivideByZeroException>(() => _calc.Divide(5, 0));
        }

        [Fact]
        public void Operations_WithNegativeNumbers_Works()
        {
            Assert.Equal(-2, _calc.Add(-5, 3));
            Assert.Equal(-8, _calc.Multiply(-2, 4));
        }

        [Fact]
        public void Operations_WithDecimals_Works()
        {
            var res = _calc.Divide(7.5, 2.5);
            Assert.Equal(3, res, precision: 6);
        }

        [Fact]
        public void Operations_WithLargeNumbers_Works()
        {
            var a = 1e12;
            var b = 2e12;
            Assert.Equal(3e12, _calc.Add(a, b));
        }
    }
}
