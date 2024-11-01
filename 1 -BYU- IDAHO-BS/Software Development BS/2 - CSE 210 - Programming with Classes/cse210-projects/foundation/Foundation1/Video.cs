using System.ComponentModel.Design.Serialization;
using System.Transactions;

public class Video{
    private string _title;
    private string _author;
    private int _length;
    private List<Comment> _coments;

    public Video(string title, string author, int length)
    {
        _title = title;
        _author = author;
        _length = length;
        _coments = new List<Comment>();
    }

    public void StoreComment(Comment comment){
        _coments.Add(comment);
    }

    public List<Comment> GetComments(){
        return _coments;
    }

    public int QuantityOfComments(){
        return _coments.Count;
    }

    public string DisplayVideo(){
        return $"Video Title: {_title} - Author: {_author} - Length: {_length}. Quantity Comments: {QuantityOfComments()}";
    }


}