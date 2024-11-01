using System;

class Program
{
    static void Main(string[] args)
    {
     
        //Running,
        Running running = new Running(30, 3);
        string rResult = running.GetSummary();  
        Console.WriteLine(rResult);

        Cycling cycling = new Cycling(60,45);
        string cResult = cycling.GetSummary();
        Console.WriteLine(cResult);

        Swimming swimming = new Swimming(60,50);
        string sResult = swimming.GetSummary();
        Console.WriteLine(sResult);


    }
}