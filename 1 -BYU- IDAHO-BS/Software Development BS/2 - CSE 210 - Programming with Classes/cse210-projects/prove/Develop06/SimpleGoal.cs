public class SimpleGoal : Goal
{
    private bool _iscomplete;
    public SimpleGoal(string shortName, string description, int points) : base(shortName, description, points)
    {
        _iscomplete = false;
    }

    public void SetCompleted(){
        _iscomplete = true;
    }

    public override void RecordEvent()
    {
        _iscomplete = true;
        Console.WriteLine($"Congratularions! You have earned {_points} points!");
    }
    public override bool IsComplete()
    {
        return _iscomplete;
    }

    public override string GetStringRepresentation()
    {
        return $"SimpleGoal:{_shortName}|{_description}|{_points}|{IsComplete()}";
    }
}