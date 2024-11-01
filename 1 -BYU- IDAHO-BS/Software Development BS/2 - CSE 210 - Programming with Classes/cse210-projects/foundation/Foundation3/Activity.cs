public abstract class Activity{
    protected int _duration;
    private string unit = "mile";
    private string _date;

   public Activity(int duration)
    {
         var eventDate = DateTime.Now;
        _date =$"{eventDate.Day} {eventDate.ToString("MMM").ToUpper()} {eventDate.Year}";;
        _duration = duration;
    }

    public abstract double GetDistance();
   
    public abstract double GetSpeed();
  
    public abstract double GetPace();

    public virtual string GetSummary()
    {
        double distance = Math.Round(GetDistance(),1);
        double speed = Math.Round(GetSpeed(),1);
        double pace = Math.Round(GetPace(),1);
        return $"> {_date} {GetType()} ({_duration}) - Distance: {distance} {unit}, Speed: {speed} mph, Pace: {pace} min per {unit}";
    }

    
}