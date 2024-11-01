using System.Security.Cryptography;

public class Menu {

    public Menu()
    {
    
    }

    public static int PresentMenu()
    {
        try
        {
            int option = 0;
            while (option <= 0 || option > 6)
            {
                Console.WriteLine("Menu options.");
                Console.WriteLine("\t1. Create new Goal.");
                Console.WriteLine("\t2. List Goals.");
                Console.WriteLine("\t3. Save Goals.");
                Console.WriteLine("\t4. Load Goals.");
                Console.WriteLine("\t5. Record Event.");
                Console.WriteLine("\t6. Quit");
                Console.WriteLine("Select a choice from menu.");
                option = int.Parse(Console.ReadLine());
            }
            return option;
           
        }
        catch(Exception)
        {
           return PresentMenu();
        }
    }

     public static string PresentGoals()
    {
        try
        {
            Console.Clear();
            int option = 0;
            while (option <= 0 || option > 3)
            {
                Console.WriteLine("The type of Goals are:");
                Console.WriteLine("\t1. Simple Goal.");
                Console.WriteLine("\t2. Eternal Goal.");
                Console.WriteLine("\t3. Checklist Goal.");
                Console.WriteLine("Which type of goal do you want to create? ");
                option = int.Parse(Console.ReadLine());
            }
            switch(option){
                case 1: 
                    return "SimpleGoal";
                case 2:
                    return "EternalGoal";
                case 3:
                    return "CheckListGoal";
                default:
                    throw new KeyNotFoundException();
            }
           
        }
        catch(Exception)
        {
           return PresentGoals();
        }
    }
}