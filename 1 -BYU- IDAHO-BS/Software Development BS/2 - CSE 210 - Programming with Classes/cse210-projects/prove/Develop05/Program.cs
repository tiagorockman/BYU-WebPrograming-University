using System;

/* I have added a functionality in the ListingActivity to prevent the same question to appear twice*/
/* I added a Try Catch Statement to protect the menu and if user type text for example it won't crash the aplication and will show the menu again.*/
/*The question of the ReflectingActivity I changed to Dictionary<int, List<string>> to get the respective question to the prompt selected*/

class Program
{
    static void Main(string[] args)
    {
        PresentMenu();
    }


    private static void ExecuteReflectingActivity()
    {
        var activity = new ReflectingActivity();
        activity.Run();
        PresentMenu();
    }

    private static void ExecuteBreathingActivity()
    {
        var activity = new BreathingActivity();
        activity.Run();
        PresentMenu();
    }

    private static void ExecuteListingActivity()
    {
        var activity = new ListingActivity();
        activity.Run();
        PresentMenu();
    }

    private static void PresentMenu()
    {
        try
        {
            Console.Clear();
            int option = 0;
            while (option <= 0 || option > 4)
            {
                Console.WriteLine("Menu options.");
                Console.WriteLine("\t1. Start breathing activity.");
                Console.WriteLine("\t2. Start reflecting activity.");
                Console.WriteLine("\t3. Start listening activity.");
                Console.WriteLine("\t4. Quit");
                Console.WriteLine("Select a choice from menu.");
                option = int.Parse(Console.ReadLine());
            }

            switch (option)
            {
                case 1:
                    ExecuteBreathingActivity();
                    break;
                case 2:
                    ExecuteReflectingActivity();
                    break;
                case 3:
                    ExecuteListingActivity();
                    break;
                case 4:
                    return;
            }
        }
        catch(Exception)
        {
            PresentMenu();
        }

    }


}