public class Word{
    private string _text;
    private bool _isHidden;

    public Word(string text){
        _text = text;
    }
    
    public void Hide(){
      var quantity =  _text.Count();
      _text = new string('_', quantity);
    }

    public void Show(){
        Console.Write(_text);
    } 
    public bool IsHideen(){
       return  _text.Contains('_');
    }

    public string GetDisplayText(){
        return _text + " ";
    }
}