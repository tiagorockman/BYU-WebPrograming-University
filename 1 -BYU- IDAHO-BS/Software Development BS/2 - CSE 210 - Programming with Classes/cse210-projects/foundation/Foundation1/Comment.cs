public class Comment{
    private string _comment;
    private string _userName;

    public Comment(string comment, string userName)
    {
        _comment = comment;
        _userName = userName;
    }

    public string DisplayComment(){
        return $"User: {_userName} commented: {_comment}";
    }
}