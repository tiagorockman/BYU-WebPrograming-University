using System.Text.Json;

/*
As additional functionalities  I added a json file to load the scriptures to a List of object.
Also I added the option to load the scripture randomically
or to list the Scriptures disposable, to that the user have to choose between 1 and 2 and I have a loop to constraint that.
Also I have a Constraint when user select from the scripture list.
*/

class Program
{
    static void Main(string[] args)
    {
        string option = "";
        JsonScriptureDTO chosenScripture = new();
        List<JsonScriptureDTO> jsonScriptureDTOs = LoadScriptures();

        do
        {
            Console.WriteLine("Type your Choice:");
            Console.WriteLine("1 - To get a Random Scripture | 2 - To list the options.");
            option = Console.ReadLine();
        } while (option != "1" && option != "2");

        if (option == "1")
            chosenScripture = GetRandomScripture(jsonScriptureDTOs);
        else
            chosenScripture = DisplayListScriptureAndSelect(jsonScriptureDTOs);


        Reference reference = new Reference(chosenScripture.Book, chosenScripture.Chapter, chosenScripture.Verse, chosenScripture.EndVerse);
        Scripture jamesScripture = new Scripture(reference, chosenScripture.Text);


        while (option != "quit")
        {
            Console.Clear();
            Console.WriteLine(jamesScripture.GetDisplayText());
            Console.WriteLine($"{Environment.NewLine} Press enter to continue or 'quit' to finish:");
            option = Console.ReadLine();

            if (jamesScripture.IsCompletelyHidden())
                option = "quit";

            jamesScripture.HideRandomWords(3);

        }

    }

    private static JsonScriptureDTO DisplayListScriptureAndSelect(List<JsonScriptureDTO> jsonScriptureDTOs)
    {
        int option = 0;
        Console.Clear();
        Console.WriteLine("Enter the number of you choice:");
        for (int i = 1; i <= jsonScriptureDTOs.Count; i++)
        {
            Console.WriteLine($"{i} - {jsonScriptureDTOs[i - 1].DisplayReference()}");
        }
        do
        {
            option = int.Parse(Console.ReadLine());
        } while (option <= 0 || option > jsonScriptureDTOs.Count);
        return jsonScriptureDTOs[option - 1];
    }

    private static JsonScriptureDTO GetRandomScripture(List<JsonScriptureDTO> jsonScriptureDTOs)
    {
        Random rand = new Random();
        int index = rand.Next(jsonScriptureDTOs.Count);
        return jsonScriptureDTOs[index];
    }

    private static List<JsonScriptureDTO> LoadScriptures()
    {
        string jsonfile = File.ReadAllText("data.json");
        return JsonSerializer.Deserialize<List<JsonScriptureDTO>>(jsonfile);
    }
}