public static class Question
{
    public static List<string> journalQuestions =
        new List<string>
       {
            "What is one small step I can take today to move closer to my long-term goals?",
            "What are my current challenges, and how can I turn them into opportunities for growth?",
            "What is something new I've learned recently that has changed my perspective?",
            "How do I define success, and is that definition still relevant to my life right now?",
            "What habits or routines are helping me, and which ones might be holding me back?",
            "Who has inspired me lately, and why?",
            "What am I most grateful for today, and how can I express that gratitude?",
            "How am I managing my work-life balance, and is there anything I need to adjust?",
            "What skill do I want to develop more, and what is my plan to work on it?",
            "How do I see myself evolving over the next five years, both personally and professionally?"
       };

    public static string GetQuestion()
    {
        var rand = new Random();
        int indexQuestion = rand.Next(0, journalQuestions.Count());
        return journalQuestions[indexQuestion];
    }
}