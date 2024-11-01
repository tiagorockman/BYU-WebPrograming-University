
public abstract class Goal
{
    protected string _shortName;
    protected string _description;
    protected int _points;

    public Goal(string shortName, string description, int points)
    {
        _shortName = shortName;
        _description = description;
        _points = points;
    }

    public abstract void RecordEvent();

    public abstract bool IsComplete();

    public abstract string GetStringRepresentation();

    public virtual bool HasBonus(){
        return false;
    }
    public virtual int GetBonus(){
        return 0;
    }
    
    public virtual string GetDetailsString()
    {
        string check = "[ ]";
        if (IsComplete())
            check = "[X]";

        return $"{check} {_shortName} ({_description})";
    }

    public string GetGoalName()
    {
        return _shortName;
    }

    public int GetPoints()
    {
        return _points;
    }

    

}