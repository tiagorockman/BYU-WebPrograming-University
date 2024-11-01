using System;

class Program
{
    
    static void Main(string[] args)
    {
        string name = "";
        int number = 0;
        DisplayWelcome();  
       name = PromptUserName();
       number = PromptUserNumber();
       number = SquareNumber(number);
        DisplayResult(name, number);
        
    }

    static void DisplayWelcome(){
        Console.WriteLine("Welcome to the program!");
    } 
    static string PromptUserName(){
        Console.Write("Please enter your name: ");
       return Console.ReadLine();
    } 
    static int PromptUserNumber(){
        Console.Write("Please enter your favorite number: ");
        return int.Parse(Console.ReadLine());
    } 
    static int SquareNumber(int number){
           return number * number;
    } 

     static void DisplayResult(string name, int number){
        Console.WriteLine($"{name}, the square of your number is {number}");
    } 

}