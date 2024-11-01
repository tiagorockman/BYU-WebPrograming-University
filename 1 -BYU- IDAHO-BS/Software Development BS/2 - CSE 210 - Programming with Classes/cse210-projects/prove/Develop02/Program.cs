using System;
using System.Reflection;
//Exceed Requirements
//On the Load method I added an option to see files names already saved before, to choose which of them the user does want to open.
class Program
{
    protected static Journal _journal = new();
    static void Main(string[] args)
    {

        int option = -1;
        Console.WriteLine("Please Select One of the following:");

        while (option != 5)
        {
            Console.WriteLine("1. Write");
            Console.WriteLine("2. Display");
            Console.WriteLine("3. Load");
            Console.WriteLine("4. Save");
            Console.WriteLine("5. Quit");
            Console.Write("What would you like to do? ");

            option = int.Parse(Console.ReadLine());

            switch (option)
            {
                case 1:
                    ActionWrite();
                    break;
                case 2:
                    ActionDisplay();
                    break;
                case 3:
                    ActionLoad();
                    break;
                case 4:
                    ActionSave();
                    break;
                default:
                    break;
            }
        }
    }

    private static void ActionSave()
    {
        Console.WriteLine("What is the filename");
        string fileName = Console.ReadLine();
        _journal.SaveToFile(fileName);
    }

    private static void ActionLoad()
    {
        try
        {
            Console.WriteLine("What is the filename, type 0 if you want to see the files name already saved before. Only .csv or .txt files.");
            string fileName = Console.ReadLine();

            if (fileName == "0")
            {
                _journal.DisplayCurrentFilesTxtAndCSVinFolder();
                Console.WriteLine("\nWhat is the filename do you choose?");
                fileName = Console.ReadLine();
            }

            _journal.LoadFromFile(fileName);

        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }

    private static void ActionDisplay()
    {
        _journal.DisplayAll();
    }

    private static void ActionWrite()
    {
        var journalContent = new JournalContent();
        string question = Question.GetQuestion();
        Console.WriteLine(question);

        journalContent.Date = DateTime.Now.ToString("dd/MM/yyyy");
        journalContent.Prompt = question;
        journalContent.Answer = Console.ReadLine();

        _journal.AddJournalContent(journalContent);
    }
}