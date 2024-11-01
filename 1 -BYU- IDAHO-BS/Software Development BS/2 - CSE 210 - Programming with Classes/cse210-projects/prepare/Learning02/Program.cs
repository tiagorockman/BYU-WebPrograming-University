using System;

class Program
{
    static void Main(string[] args)
    {
       Job job1 = new Job();
       job1._jobTitle = "Software Engineer";
       job1._companyName = "Microsoft";
       job1._experienceStartingYear = "2019";
       job1._experienceEndingYear = "2022";

        job1.DisplayJobDetails();


       Job job2 = new Job();
       job2._jobTitle = "Front-End Developer";
       job2._companyName = "Apple";
          job2._experienceStartingYear = "2022";
       job2._experienceEndingYear = "2023";

       job2.DisplayJobDetails();

       Resume resume = new Resume();
       resume._personName = "James Snow";
       resume._jobs.Add(job1);
       resume._jobs.Add(job2);

       resume.DisplayResumeInformation();
       
    }
}