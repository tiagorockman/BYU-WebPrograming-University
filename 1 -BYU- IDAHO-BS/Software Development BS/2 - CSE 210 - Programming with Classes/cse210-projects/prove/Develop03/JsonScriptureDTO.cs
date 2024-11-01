public class JsonScriptureDTO
{
    public string Book { get; set; }
    public int Chapter { get; set; }
    public int Verse { get; set; }
    public int EndVerse { get; set; }
    public string Text { get; set; }

    public string DisplayReference(){
        if(EndVerse == 0)
            return $"{Book} {Chapter}:{Verse}";
        else
            return $"{Book} {Chapter}:{Verse}-{EndVerse}";
    }
    
}