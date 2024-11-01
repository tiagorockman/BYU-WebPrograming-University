public class ReflectingActivity : Activity
{
    private List<string> _prompts;
    private Dictionary<int, List<string>> _questions;
    private int _idRandomSelected;

    public ReflectingActivity()
    {
        _prompts = new List<string>
        {
            "Can you recall a difficult time in your life when you overcame a challenge? How did you get through it?",
            "What strengths did you discover within yourself during a tough experience?",
            "How did you handle stress or fear during your most challenging moments?",
            "What were the thoughts or beliefs that kept you going during difficult times?",
            "Who or what supported you when you faced adversity? How did they help?",
            "How did overcoming past challenges shape the person you are today?",
            "What lessons did you learn from a situation where things did not go as planned?",
            "How do you typically respond when things don’t go the way you expect? Can you think of a time you handled it well?",
            "Can you identify a situation where failure made you stronger? How did it prepare you for the future?",
            "When was the last time you surprised yourself with your ability to adapt or persevere?",
            "How do you practice self-compassion when life gets hard?",
            "What qualities do you admire in yourself for the way you handled difficult situations in the past?",
            "Looking back, what advice would you give yourself during a tough moment in your life?",
            "What habits or routines help you build resilience in your day-to-day life?",
            "How do you stay motivated during long-term challenges or projects?",
            "What personal strengths can you rely on when facing future challenges?",
            "What role does failure play in building your resilience?",
            "How do you bounce back emotionally after setbacks?",
            "Can you think of a situation where you had to change your mindset to overcome a challenge?",
            "How can you apply the strength you have shown in the past to current or future challenges?"
        };

        _questions = new Dictionary<int, List<string>>
        {
            { 1, new List<string> {
                "Can you recall a difficult time in your life when you overcame a challenge? How did you get through it?",
                "What emotions did you feel during that time, and how did you manage them?",
                "Looking back, would you handle the situation differently now?"
            }},
            { 2, new List<string> {
                "What strengths did you discover within yourself during a tough experience?",
                "Have you always had these strengths, or did the situation help you develop them?",
                "How can you use these strengths more intentionally moving forward?"
            }},
            { 3, new List<string> {
                "How did you handle stress or fear during your most challenging moments?",
                "Were there any specific tools or practices that helped you stay grounded?",
                "How do you typically react to fear now, and is there room for improvement?"
            }},
            { 4, new List<string> {
                "What were the thoughts or beliefs that kept you going during difficult times?",
                "How did your mindset change from the beginning to the end of the challenge?",
                "What beliefs can you hold onto for future challenges?"
            }},
            { 5, new List<string> {
                "Who or what supported you when you faced adversity? How did they help?",
                "Have you expressed gratitude to those who supported you? If not, how could you?",
                "How can you create a similar support system for yourself moving forward?"
            }},
            { 6, new List<string> {
                "How did overcoming past challenges shape the person you are today?",
                "What personal qualities or values emerged from these experiences?",
                "In what ways do you think you are stronger now than before?"
            }},
            { 7, new List<string> {
                "What lessons did you learn from a situation where things did not go as planned?",
                "How have these lessons influenced your decisions since then?",
                "Can you think of a recent situation where you applied one of these lessons?"
            }},
            { 8, new List<string> {
                "How do you typically respond when things don’t go the way you expect? Can you think of a time you handled it well?",
                "What could you do differently next time you encounter an unexpected situation?",
                "How can you develop a more positive response to setbacks?"
            }},
            { 9, new List<string> {
                "Can you identify a situation where failure made you stronger? How did it prepare you for the future?",
                "How do you now define success and failure based on that experience?",
                "What did you learn about yourself from that failure?"
            }},
            { 10, new List<string> {
                "When was the last time you surprised yourself with your ability to adapt or persevere?",
                "What skills or mindset shifts helped you adapt?",
                "How can you cultivate these skills to handle future challenges?"
            }},
            { 11, new List<string> {
                "How do you practice self-compassion when life gets hard?",
                "What is one kind thing you can say to yourself right now?",
                "How would you treat a friend going through a similar experience?"
            }},
            { 12, new List<string> {
                "What qualities do you admire in yourself for the way you handled difficult situations in the past?",
                "How can you nurture these qualities moving forward?",
                "What new qualities would you like to develop?"
            }},
            { 13, new List<string> {
                "Looking back, what advice would you give yourself during a tough moment in your life?",
                "How would that advice have changed the outcome or your experience?",
                "What advice can you give yourself right now for current challenges?"
            }},
            { 14, new List<string> {
                "What habits or routines help you build resilience in your day-to-day life?",
                "Which habit do you find the most challenging to maintain, and why?",
                "What new habit could you adopt to strengthen your resilience?"
            }},
            { 15, new List<string> {
                "How do you stay motivated during long-term challenges or projects?",
                "What strategies work best for you when motivation is low?",
                "Who or what inspires you to keep going?"
            }},
            { 16, new List<string> {
                "What personal strengths can you rely on when facing future challenges?",
                "How can you strengthen these abilities even further?",
                "What additional strengths would you like to develop?"
            }},
            { 17, new List<string> {
                "What role does failure play in building your resilience?",
                "How do you reframe failure into a learning opportunity?",
                "How can you encourage others to embrace failure as part of growth?"
            }},
            { 18, new List<string> {
                "How do you bounce back emotionally after setbacks?",
                "What emotions do you typically experience, and how do you manage them?",
                "What rituals or practices help you recover more quickly?"
            }},
            { 19, new List<string> {
                "Can you think of a situation where you had to change your mindset to overcome a challenge?",
                "What thoughts or beliefs did you let go of to move forward?",
                "How can you maintain a growth mindset in future challenges?"
            }},
            { 20, new List<string> {
                "How can you apply the strength you have shown in the past to current or future challenges?",
                "What is one thing you can do today to prepare for future difficulties?",
                "What reminder or mantra can you use when facing new challenges?"
            }}
        };
    }

    public void Run()
    {
        _name = "Reflecting Activity";
        _description = @"This activity will help you reflect on times in your life when you have shown strength and 
        resilience. This will help you recognize the power you have and how you can use it in other aspects of your life.";

        DisplayStartingMessage();

        int timeSpinner = Math.Abs(_duration / 2);
        Console.Clear();
        base.DisplayGetReady(5);
        Console.WriteLine("\nConsider the following prompt:");
        DisplayPrompt();
        Console.WriteLine("\nWhen you have something in mind, press enter to continue.");
        Console.ReadLine();
        Console.WriteLine("\nNow ponder on each of the following questions as they related to this experience.");
        Console.Write("You may begin in: ");
        ShowCountDown(4);
        DateTime now = DateTime.Now;
        DateTime endTime = now.AddSeconds(_duration);
        while (DateTime.Now < endTime)
        {
            Console.Clear();
            DisplayQuestion(1);
            ShowSpinner(timeSpinner);
            DisplayQuestion(2);
            ShowSpinner(timeSpinner);
        }
        DisplayEndingMessage();
    }
    public string GetRandomPrompt()
    {
        return ReturnRandom(_prompts);
    }
    public string GetRandomQuestion()
    {
       _ = _questions.TryGetValue(_idRandomSelected, out List<string> questionsLocal);
        return ReturnRandom(questionsLocal, false);
    }

    private string ReturnRandom(List<string> list, bool remove = true)
    {
        Random random = new Random();
        int id = random.Next(0, list.Count);
        string prompt = list[id];
        _idRandomSelected = id;
        if(remove)
            list.RemoveAt(id);
        return prompt;
    }

    public void DisplayPrompt()
    {
        Console.WriteLine($"\n--- {GetRandomPrompt()} ---");
    }
    public void DisplayQuestion(int line)
    {
        if (line == 1)
            Console.Write($"\n\n> {GetRandomQuestion()} ");
        else
            Console.Write($"\n> {GetRandomQuestion()} \n");
    }

}