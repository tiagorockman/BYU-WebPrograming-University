using System.Linq;
using System.Security.Cryptography.X509Certificates;

public class Scripture{
    private Reference _reference;
    private List<Word> _words = new();

    public Scripture(Reference reference, string text)
    {
        _reference = reference;
        foreach(var word in text.Split(' ')){
            Word wordObject = new Word(word);
            _words.Add(wordObject);
        }
    }

    public void HideRandomWords(int NumberToHide){
       
        while(NumberToHide >= 0){
            RandomHide();            
            NumberToHide--;
        }
    }

    private void RandomHide(){
        Random rand = new Random();
        // List<Word> avilableWords = GetAvailableWords();
        // int index = rand.Next(avilableWords.Count);
        // _words[avilableWords[index]].Hide();
        // return index;


        var availableWordIndices = _words
            .Select((w, index) => new { Word = w, Index = index })
            .Where(w => !w.Word.IsHideen()) // Only words that are not hidden
            .Select(w => w.Index)           // Keep their original indices
            .ToList();

        if(availableWordIndices.Count > 0){
            // Select a random index from the available ones
            int randomIndex = rand.Next(availableWordIndices.Count);

            // Hide the word in the original list using the selected index
            _words[availableWordIndices[randomIndex]].Hide();
        
        }
    }

    private List<Word> GetAvailableWords(){
       return _words.Where(w=> !w.IsHideen()).ToList();
    }

    public string GetDisplayText(){
        string result = _reference.GetDisplayText();
        foreach(var word in _words){
            result += word.GetDisplayText();
        }
        return result;
    }

    public bool IsCompletelyHidden(){
        return _words.Where(w => w.IsHideen() == false).Count() == 0;
    }
}