public class Cycling : Activity
{

    private double _speed;

    public Cycling(int duration, int speed) : base(duration)
    {
        _speed = speed;
    }

    public override double GetDistance()
    {
        double result = _speed * 50 / 1000 * 0.62;
        return result;
    }

    public override double GetPace()
    {
        return 60/ _speed;
    }

    public override double GetSpeed()
    {
        return _speed;
    }
}