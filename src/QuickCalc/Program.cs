using System;
using QuickCalcLib;

class Program
{
    static void Main(string[] args)
    {
        var calc = new CalculatorState();
        Console.WriteLine("Quick-Calc (console) — enter sequences programmatically or run tests.");
        Console.WriteLine("This console is minimal; use tests for verification.");
        Console.WriteLine("Press Enter to exit.");
        Console.ReadLine();
    }
}
