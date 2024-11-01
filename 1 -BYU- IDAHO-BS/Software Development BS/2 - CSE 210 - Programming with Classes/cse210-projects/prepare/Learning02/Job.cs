public class Job
{
    public string _jobTitle;
    public string _companyName;
    public string _experienceStartingYear;
    public string _experienceEndingYear;

    public void DisplayJobDetails(){
        Console.WriteLine($"{_jobTitle} ({_companyName}) {_experienceStartingYear}-{_experienceEndingYear} ");
    }
}