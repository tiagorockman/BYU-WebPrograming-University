using System;

class Program
{
    static void Main(string[] args)
    {
        //1/1
        Fraction fraction = new Fraction();
        Console.WriteLine(fraction.GetFractionString());
        Console.WriteLine(fraction.GetDecimalValue());

        //6/1
        Fraction fraction6_1= new Fraction(6);
         Console.WriteLine(fraction6_1.GetFractionString());
        Console.WriteLine(fraction6_1.GetDecimalValue());
        //3/4
        Fraction fraction3_4 = new Fraction(3,4);
        Console.WriteLine(fraction3_4.GetFractionString());
        Console.WriteLine(fraction3_4.GetDecimalValue());

        //1/3
         Fraction fraction1_3 = new Fraction(1,3);
        Console.WriteLine(fraction1_3.GetFractionString());
        Console.WriteLine(fraction1_3.GetDecimalValue());

    }
}