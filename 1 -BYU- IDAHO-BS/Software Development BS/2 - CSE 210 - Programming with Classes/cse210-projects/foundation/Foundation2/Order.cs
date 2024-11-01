public class Order
{
    private List<Product> _products = new List<Product>();
    private Customer _customer;

    public Order(List<Product> products, Customer customer)
    {
        _products = products;
        _customer = customer;
    }

    public double TotalCost()
    {
        double totalValuefromProduct = _products.Sum(x => x.TotalCost());
        if (_customer.WithinUS())
            return Math.Round(totalValuefromProduct + 5, 2);
        else
            return Math.Round(totalValuefromProduct + 35, 2);
    }

    public void DisplayPackingLabel()
    {
        _products.ForEach(p =>
        {
            Console.WriteLine($"ID: {p.GetId()} - Name: {p.GetName()}");
        });
    }


    public void DisplayShippingLabel()
    {
        Console.WriteLine($"ID: {_customer.GetName()} - {_customer.GetAddress()}");
    }

}