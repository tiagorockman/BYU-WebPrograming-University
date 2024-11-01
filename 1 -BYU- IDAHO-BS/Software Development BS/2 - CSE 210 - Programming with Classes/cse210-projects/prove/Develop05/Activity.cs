public class Activity{
    protected string _name;
    protected string _description;
    protected int _duration;

    public Activity()
    {
       
    }

    public void DisplayStartingMessage(){
        Console.Clear();
        Console.WriteLine($"Welcome to the {_name}\n");
        Console.WriteLine(_description);
        Console.Write("\nHow long, in seconds, would you like for your session? ");
        _duration = int.Parse(Console.ReadLine());
    }

    public void DisplayEndingMessage(){
        DisplayWellDone(6);
        Console.WriteLine($"\nYou have completed another {_duration} seconds of the {_name}");
        ShowSpinner(10);
    }

      public void DisplayWellDone(int seconds){
        Console.WriteLine("\nWell Done!!");
        ShowSpinner(seconds);
    }


    public void DisplayGetReady(int seconds){
        Console.WriteLine("Get Ready...");
        ShowSpinner(seconds);
    }

    public void ShowSpinner(int seconds){
        int i = 0;
        List<string> animationStrings = new List<string>(){
            "|",
            "/",
            "-",
            "\\",
            "|",
            "/",
            "-",
            "\\"
        };

       while(seconds > 0){
        string s = animationStrings[i];
        Console.Write(s);
        Thread.Sleep(1000);
        Console.Write("\b \b");
        seconds--;
        i++;
        if(i >= animationStrings.Count)
            i = 0;
       }
    }
    public void ShowCountDown(int seconds){
        while(seconds >0){
            Console.Write(seconds);
            Thread.Sleep(1000);
            Console.Write("\b \b");
            seconds--;
        }
    }

}