public class Swimming : Activity
{

    private int _swimmingLaps;

    public Swimming(int duration, int swimmingLaps) : base(duration)
    {
        _swimmingLaps = swimmingLaps;
    }

    public override double GetDistance()
    {
       double result = _swimmingLaps * 50 / 1000 * 0.62; 
       return result;
    }

    public override double GetPace()
    {
        double result = _duration/GetDistance();
        return result;
    }

    public override double GetSpeed()
    {
        double result = (GetDistance()/_duration) *60;
        return result;
    }
}