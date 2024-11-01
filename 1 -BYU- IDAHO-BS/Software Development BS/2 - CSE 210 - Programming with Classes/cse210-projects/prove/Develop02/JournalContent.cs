public class JournalContent
{
  public string Date;
  public string Prompt;
  public string Answer;

    public JournalContent()
    {
    }

    public JournalContent(string line)
  {
    string[] pos = line.Split("|");
    Date = pos[0];
    Prompt = pos[1];
    Answer = pos[2];
  }


  public void Display()
  {
    Console.WriteLine($"Date: {Date} - Prompt: {Prompt}");
    Console.WriteLine(Answer + Environment.NewLine);
  }

}