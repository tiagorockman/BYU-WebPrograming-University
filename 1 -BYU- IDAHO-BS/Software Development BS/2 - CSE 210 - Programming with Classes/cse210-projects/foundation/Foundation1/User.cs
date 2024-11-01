public class User{
    private Guid _id;
    private string _name;

    public User(string name)
    {
        _id = new Guid();
        _name = name;
    }

    public string GetUserName(){
       return _name;
    }
}