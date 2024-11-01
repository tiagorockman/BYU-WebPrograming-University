using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        int number = -1;
        List<int> numberList = new List<int>();
        Console.WriteLine("\t\tEnter a list of numbers, type 0 when finished.");
        do{
            Console.WriteLine("Enter number: ");
            number = int.Parse(Console.ReadLine());
            numberList.Add(number);
        }while(number != 0);

        numberList.RemoveAt(numberList.IndexOf(0));
        Console.WriteLine($"\nThe sum is {numberList.Sum(x=>x)}");
        Console.WriteLine($"\nThe average is {Math.Round(numberList.Average(), 3)}");     
        Console.WriteLine($"\nThe smallest positive number is {GetSmallestPositiveNumber(numberList)}");
        Console.WriteLine($"\nThe sorted list is:");
        numberList.Sort();
        numberList.ForEach(d=> { 
            if(d !=0)
                Console.WriteLine(d);
        });
    }

    static int GetSmallestPositiveNumber(List<int> numberList){
        int lowerNumber = numberList.Max(x=>x);
        foreach(var number in numberList){
            if(number >0){
                if(number < lowerNumber)
                    lowerNumber = number;
            }
        }
        return lowerNumber;
    }
}