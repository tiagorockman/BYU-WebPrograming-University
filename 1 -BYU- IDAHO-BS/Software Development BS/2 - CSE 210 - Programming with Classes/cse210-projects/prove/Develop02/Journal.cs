public class Journal
{
    private List<JournalContent> _journalContents = [];
    public void AddJournalContent(JournalContent journalContent)
    {
        _journalContents.Add(journalContent);
    }

    public void DisplayAll()
    {
        foreach (var ans in _journalContents)
        {
            ans.Display();
        }
    }

    internal void DisplayCurrentFilesTxtAndCSVinFolder()
    {
        var files = Directory.GetFiles(Directory.GetCurrentDirectory());
        foreach (var selectedFile in files) //select only files with txt in the name
        {
            string fileName = Path.GetFileName(selectedFile);
            if (selectedFile.Contains(".txt") || selectedFile.Contains(".csv"))
                Console.Write($" {fileName} |");
        }
    }

    internal void LoadFromFile(string fileName)
    {
        _journalContents.Clear();

        string[] lines = System.IO.File.ReadAllLines(fileName);
        foreach (var line in lines)
        {
            JournalContent journal = new JournalContent(line);
            _journalContents.Add(journal);
        }
    }

    internal void SaveToFile(string fileName)
    {
        using (var writer = new StreamWriter(fileName))
        {
            foreach (var journal in _journalContents)
            {
                writer.WriteLine($"{journal.Date}|{journal.Prompt}|{journal.Answer}");
            }
        }
    }
}