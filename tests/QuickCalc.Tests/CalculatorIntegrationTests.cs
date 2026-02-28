using Xunit;
using QuickCalcLib;

namespace QuickCalc.Tests
{
    public class CalculatorIntegrationTests
    {
        [Fact]
        public void FullUserFlow_Addition_ShowsCorrectResult()
        {
            var state = new CalculatorState();
            state.EnterNumber("5");
            state.PressOperator("+");
            state.EnterNumber("3");
            state.PressEquals();
            Assert.Equal("8", state.Display);
        }

        [Fact]
        public void ClearAfterCalculation_ResetsDisplay()
        {
            var state = new CalculatorState();
            state.EnterNumber("9");
            state.PressOperator("*");
            state.EnterNumber("9");
            state.PressEquals();
            Assert.Equal("81", state.Display);
            state.PressClear();
            Assert.Equal("0", state.Display);
        }

        [Fact]
        public void DivideByZero_FromState_ShowsError()
        {
            var state = new CalculatorState();
            state.EnterNumber("5");
            state.PressOperator("/");
            state.EnterNumber("0");
            state.PressEquals();
            Assert.Equal("Error", state.Display);
        }
    }
}
