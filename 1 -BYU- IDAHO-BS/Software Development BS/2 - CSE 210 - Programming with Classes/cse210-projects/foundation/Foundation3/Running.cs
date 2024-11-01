public class Running : Activity
{
    private double _distance;
    
 public Running(int duration, double distance) : base(duration)
    {
        _distance = distance;
    }

    public override double GetDistance()
    {
        return _distance;
    }

    public override double GetSpeed()
    {
        return _distance/_duration*60;
    }

    public override double GetPace()
    {
        return 60/GetSpeed();
    }
}