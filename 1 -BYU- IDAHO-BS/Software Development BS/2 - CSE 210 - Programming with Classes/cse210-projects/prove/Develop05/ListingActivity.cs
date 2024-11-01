public class ListingActivity : Activity{
    private List<string> _userAnswers;
    private List<String> _prompts;

    public ListingActivity()
    {
        _userAnswers = new List<string>();
        _prompts = new List<string>(){
            "What are the things in my life that truly bring me joy?",
            "Am I spending enough time with the people I care about?",
            "What is one habit I could change to improve my well-being?",
            "Am I holding onto grudges that I need to let go of?",
            "What am I grateful for today that I often take for granted?",
            "What would I do differently if I knew no one would judge me?",
            "Am I investing my time in things that align with my long-term goals?",
            "How do I react when things don’t go my way? Can I improve?",
            "Who inspires me, and why? What qualities do I admire in them?",
            "What fears are holding me back from reaching my full potential?",
            "When was the last time I stepped out of my comfort zone?",
            "Am I listening to understand, or just waiting for my turn to speak?",
            "How do I respond to criticism? Am I open to learning from it?",
            "Am I being kind to myself, or am I too hard on myself?",
            "What legacy do I want to leave behind when I’m gone?",
            "Am I making time to learn and grow every day?",
            "How do I contribute to the well-being of others around me?",
            "What do I need to forgive myself for?",
            "Am I living the life I want, or the life others expect of me?",
            "What can I do today that my future self will thank me for?",
            "When have you felt the Holy Ghost this month?"
        };
    }
    public void Run(){
        _name=$"Listing Activity";
        _description = @"This activity will help you reflect on the good things in your life by having you list as many things
        as you can in a certain area.";

        DisplayStartingMessage();
       
        Console.Clear();
        base.DisplayGetReady(5);
        Console.WriteLine("\nList as many responses you can to the following prompt:\n");
        
        GetRandomPrompt();
        ShowCountDown(4);
        DateTime now = DateTime.Now;
        DateTime endTime = now.AddSeconds(_duration);        
        while(DateTime.Now < endTime){             
            Console.Write("> ");
           string text = Console.ReadLine();
           _userAnswers.Add(text);
        }    
        Console.WriteLine($"You listed {_userAnswers.Count} items!");
        DisplayEndingMessage();
    }
    public void GetRandomPrompt(){
        Random random =  new Random();
        int rndValue = random.Next(0, _prompts.Count);
        Console.WriteLine($" --- {_prompts[rndValue]} ---");
        //prevent the same question appears again.
        _prompts.RemoveAt(rndValue);
        Console.Write("You may begin in: ");
    }
    public List<String> GetListFromUser(){
        return _userAnswers;
    }

}