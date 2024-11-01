public class BreathingActivity : Activity{
    public BreathingActivity()
    {
        
    }

    public void Run(){
         _name=$"Breathing Activity";
        _description = @"This activity will help you relax by walking your through 
        breathin in and out slowly. Clear your mind and focus on your breathing";

        DisplayStartingMessage();
       
        Console.Clear();
        base.DisplayGetReady(5);
         DateTime now = DateTime.Now;
        DateTime endTime = now.AddSeconds(_duration);
        while(DateTime.Now < endTime){             
             Console.Write("\n\nBreathe in...");
             ShowCountDown(4);
             Console.Write("\nNow you breathe out...");
             ShowCountDown(6);
        }    
        DisplayEndingMessage();
    }
}