public class CheckListGoal : Goal
{
    private int _amountCompleted;
    private int _target;
    private int _bonus;

    public CheckListGoal(string shortName, string description, int points, int target, int bonus, int amountCompleted = 0) : base(shortName, description, points)
    {
        _amountCompleted = amountCompleted;
        _target = target;
        _bonus = bonus;
    }

    public override bool HasBonus()
    {
        return true;
    }

    public override void RecordEvent()
    {
        _amountCompleted++;
        if(_amountCompleted > _target){
            Console.WriteLine("You have already completed this Goal");
            return;
        }

        if (_amountCompleted < _target)
        {
            Console.WriteLine($"Congratularions! You have earned {_points} points!");
        }
        else{
             Console.WriteLine($"Congratularions! You have earned {_bonus} of Bonus for completing this Goal!");
        }
    }
    public override bool IsComplete()
    {
        return _target == _amountCompleted;
    }

    public override string GetStringRepresentation()
    {
        return $"CheckListGoal:{_shortName}|{_description}|{_points}|{_bonus}|{_target}|{_amountCompleted}";
    }

    public override string GetDetailsString()
    {
        string name_description = base.GetDetailsString();
        return $"{name_description} -- currently completed: {_amountCompleted}/{_target}";
    }

    public override int GetBonus()
    {
        return _bonus;
    }
}