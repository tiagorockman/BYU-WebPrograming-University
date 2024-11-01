class Resume
{
    public string _personName;
    public List<Job> _jobs = [];

    public void DisplayResumeInformation(){
        Console.WriteLine($"\nName: {_personName}");
        Console.WriteLine("Jobs:");
        foreach(var job in _jobs){
            Console.WriteLine($"{job._jobTitle} ({job._companyName}) {job._experienceStartingYear}-{job._experienceEndingYear} ");
        }
    }
}