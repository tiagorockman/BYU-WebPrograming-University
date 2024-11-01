using System;

class Program
{
    static void Main(string[] args)
    {
        bool keepPlaying = true;

        while(keepPlaying){
            Random randomGenerator = new Random();
            int magicNumber = randomGenerator.Next(1,100);
            int guessNumber = 0;
            int guessCounter = 1;
            do {
                Console.WriteLine("\nWhat is your guess?");
                guessNumber = int.Parse(Console.ReadLine());
                if(guessNumber > magicNumber){
                    Console.WriteLine("Lower");
                    guessCounter++;
                }else if(guessNumber < magicNumber){
                    Console.WriteLine("Higher");
                    guessCounter++;
                }else{
                    Console.WriteLine("\nYou guessed it!");
                    Console.WriteLine($"You spent {guessCounter} times to guess it!");

                    Console.WriteLine("\nDo you want to keep playing? 1 - [YES] 0 - [NO] ");
                    int response = int.Parse(Console.ReadLine());
                    keepPlaying = response == 1 ? true : false; 
                }
            } while (guessNumber != magicNumber);
        }      
             
    }
}