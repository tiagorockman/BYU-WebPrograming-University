public class Product
{
    private Guid _productID;
    private double _price;
    private int _quantity;
    private string _name;

    public Product(double price, int quantity, string name)
    {
        _productID = Guid.NewGuid();
        _name = name;
        _price = price;
        _quantity = quantity;
    }

    public double TotalCost()
    {
        return _price * _quantity;
    }

    public string GetName()
    {
        return _name;
    }
    public string GetId()
    {
        return _productID.ToString();
    }


}