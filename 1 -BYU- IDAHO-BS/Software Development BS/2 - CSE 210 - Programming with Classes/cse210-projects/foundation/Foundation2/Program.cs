using System;

class Program
{
    static void Main(string[] args)
    {
        Address address1 = new Address("123 Maple St", "Springfield", "Illinois", "USA");
        Address address2 = new Address("456 Oak Ave", "Toronto", "Ontario", "Canada");
        Address address3 = new Address("789 Pine Blvd", "Brisbane", "Queensland", "Australia");

        // Now, create the Customer instances using the addresses
        Customer customer1 = new Customer("John Smith", address1);
        Customer customer2 = new Customer("Emily Davis", address2);
        Customer customer3 = new Customer("Lucas Taylor", address3);

         Product product1 = new Product(19.99, 10, "Wireless Mouse");
        Product product2 = new Product(149.99, 5, "Mechanical Keyboard");
        Product product3 = new Product(399.99, 2, "Gaming Monitor");
        Product product4 = new Product(49.99, 20, "USB-C Hub");
        Product product5 = new Product(29.99, 15, "Portable Charger");
        Product product6 = new Product(999.99, 1, "High-End Graphics Card");

            // Orders
            
        List<Product> order1Products = new List<Product> { product1, product2, product4 };
        List<Product> order2Products = new List<Product> { product3, product5, product6 };
        List<Product> order3Products = new List<Product> { product1, product3, product5 };

        Order order1 = new Order(order1Products, customer1);
        Order order2 = new Order(order2Products, customer2);
        Order order3 = new Order(order3Products, customer3);

        foreach(var item in new List<Order>{ order1, order2, order3}){
            Console.WriteLine($"\n");
            item.DisplayShippingLabel();
            Console.WriteLine("Products");
            item.DisplayPackingLabel();
            Console.Write("TotalPrice: ");
            Console.Write(item.TotalCost());
        }



    }
}