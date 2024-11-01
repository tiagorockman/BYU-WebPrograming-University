public class GoalManager
{
    private List<Goal> _goals;
    private int _score;

    public GoalManager()
    {
        _goals = new List<Goal>();
        _score = 0;

    }

    public void Start()
    {
        DisplayPlayorinfo();
        int option = Menu.PresentMenu();

        switch (option)
        {
            case 1:
                CreateGoal();
                break;
            case 2:
                ListGoalDetails();
                break;
            case 3:
                SaveGoals();
                break;
            case 4:
                LoadGoals();
                break;
            case 5:
                RecordEvent();
                break;
            case 6:
                return;
        }

    }

    private void DefineGoalByType(string goaltype, string goalName, string shortDescription, int score, int target = 0, int bonus = 0, int ammountCompleted = 0, bool completed = false)
    {
        switch (goaltype)
        {
            case "SimpleGoal":
                SimpleGoal simpleGoal = new SimpleGoal(goalName, shortDescription, score);
                _goals.Add(simpleGoal);
                if (completed)
                    simpleGoal.SetCompleted();
                break;
            case "EternalGoal":
                EternalGoal eternalGoal = new EternalGoal(goalName, shortDescription, score);
                _goals.Add(eternalGoal);
                break;
            case "CheckListGoal":
                CheckListGoal checkListGoal = new CheckListGoal(goalName, shortDescription, score, target, bonus, ammountCompleted);
                _goals.Add(checkListGoal);
                break;

        }
    }
    public void DisplayPlayorinfo()
    {
        Console.Clear();
        Console.WriteLine($"\nYou have {_score} points.\n");
    }

    public void ListGoalNames()
    {
        foreach (var (goal, index) in _goals.Select((item, index) => (item, index)))
        {
            Console.WriteLine($"\t{index + 1}. {goal.GetGoalName()}");
        }
    }
    public void ListGoalDetails()
    {
        Console.WriteLine("The goals are:");
        //using for each with the index
        foreach (var (goal, index) in _goals.Select((item, index) => (item, index)))
        {
            Console.WriteLine($"\t{index + 1}. {goal.GetDetailsString()}");
        }
        Console.WriteLine("Press any key to continue...");
        Console.ReadLine();
        Start();
    }
    public void CreateGoal()
    {
        int target = 0; int bonus = 0;
        string goaltype = Menu.PresentGoals();
        Console.WriteLine("What is the name of your goal? ");
        string goalName = Console.ReadLine();
        Console.WriteLine("What is a short description of it? ");
        string shortDescription = Console.ReadLine();
        Console.WriteLine("What is the ammount of points associated with this goal? ");
        int score = int.Parse(Console.ReadLine());
        if (goaltype == "CheckListGoal")
        {
            Console.WriteLine("How many times this goal need to be accomplished for a bonus? ");
            target = int.Parse(Console.ReadLine());
            Console.WriteLine("What is the bonus for accomplish it that many times? ");
            bonus = int.Parse(Console.ReadLine());
        }
        DefineGoalByType(goaltype, goalName, shortDescription, score, target, bonus);

        Start();

    }
    public void RecordEvent()
    {
        ListGoalNames();
        Console.WriteLine("Which goal did you accomplish?");
        int option = int.Parse(Console.ReadLine());

        var goal = _goals[option - 1];
        goal.RecordEvent();
        if (goal.IsComplete() && goal.HasBonus())
        {
            _score += goal.GetBonus();
        }
        else
        {
            _score += goal.GetPoints();
        }


        Console.WriteLine($"You now have {_score} points.");

        Console.WriteLine("\nPress any key to continue...");
        Console.ReadLine();

        Start();
    }
    public void SaveGoals()
    {
        Console.WriteLine("What is the filename for the goal file? ");
        string filename = Console.ReadLine();
        using (var streamWriter = new StreamWriter(filename))
        {
            streamWriter.WriteLine(_score);
            foreach (var item in _goals)
            {
                streamWriter.WriteLine($"{item.GetStringRepresentation()}");
            }
        }

        Start();
    }
    public void LoadGoals()
    {
        try
        {
            Console.WriteLine("What is the filename for the goal file? ");
            string filename = Console.ReadLine();
            string[] lines = File.ReadAllLines(filename);
            _score = int.Parse(lines[0]); //getFirstLine

            int target = 0;
            int bonus = 0;
            int amount = 0;
            bool completed = false;
            foreach (var line in lines)
            {
                if (lines.First() == line)
                    continue;

                string[] columns = line.Split("|");
                string[] parts = columns[0].Split(":");

                string type = parts[0];
                string name = parts[1];
                string description = columns[1];
                int points = int.Parse(columns[2]);

                if (type == "SimpleGoal")
                {
                    if (columns[3] == "True")
                        completed = true;
                }


                if (type == "CheckListGoal")
                {
                    bonus = int.Parse(columns[3]);
                    target = int.Parse(columns[4]);
                    amount = int.Parse(columns[5]);

                }

                DefineGoalByType(type, name, description, points, target, bonus, amount, completed);

            }

            Start();

        }
        catch (FileNotFoundException)
        {
            Console.Clear();
            Console.WriteLine("Erro ao encontrar arquivo");
        }
        catch (Exception ex)
        {
            Console.Clear();
            Console.WriteLine($"Erro: {ex}");
        }


    }

}