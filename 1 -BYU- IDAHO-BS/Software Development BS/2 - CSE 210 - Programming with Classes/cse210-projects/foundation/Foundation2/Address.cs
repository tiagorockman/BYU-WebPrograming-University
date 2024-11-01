public class Address{
    private string _street;
    private string _city;
    private string _stateProvince;
    private string _country;

    public Address(string street, string city, string stateProvince, string country)
    {
        _street = street;
        _city = city;
        _stateProvince = stateProvince;
        _country = country;
    }

     public bool WithinUS(){
        return _country == "US";
    }

    public string DisplayAddress(){
        return $"Street: {_street} City: {_city} \nState: {_stateProvince} Country: {_country}";
    }
}