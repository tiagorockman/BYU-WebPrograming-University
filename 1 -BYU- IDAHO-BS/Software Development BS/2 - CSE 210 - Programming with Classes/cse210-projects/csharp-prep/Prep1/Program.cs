using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("What is your first name?");
        string firstName = Console.ReadLine();

        Console.WriteLine("What is your last name?");
        string lastName = Console.ReadLine();
        
        Console.WriteLine($"Your name is {FirsLetterUpper(lastName)}, {FirsLetterUpper(firstName)} {FirsLetterUpper(lastName)}.");


    }

    static string FirsLetterUpper(string text) =>
        text switch
        {
             null => throw new ArgumentNullException(nameof(text)),
            "" => throw new ArgumentException($"{nameof(text)} cannot be empty", nameof(text)),
            _ => string.Concat(text[0].ToString().ToUpper(), text.AsSpan(1).ToString().ToLower())
        };
    
}