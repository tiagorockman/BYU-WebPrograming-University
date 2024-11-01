using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Inform your grade percentage!");
        string stringGrade = Console.ReadLine();
        int grade = Int32.Parse(stringGrade);

        (bool aproved, string letter) = StudentStatusDefine(grade);

        Console.WriteLine($"Your grade is {letter}.");
        if(aproved)
            Console.WriteLine($"Congratulations! You're approved!");
        else
            Console.WriteLine($"Keep Working! You can do a better job next time.");



    }

    static (bool,string) StudentStatusDefine(int grade){
        string letter = "";
        string letterSignal = "";
        if(grade >=90){
            letter = "A";
            letterSignal= GetLetterSignal(grade);
            if(letterSignal != "+")
               letter = letter + letterSignal;
            return (true, letter);
        }else if (grade >=80){
            letter = "B";
            letterSignal= GetLetterSignal(grade);
            return (true, letter + letterSignal);
        }else if(grade >= 70){
            letter = "C";
            letterSignal= GetLetterSignal(grade);
            return (true, letter + letterSignal);
        }else if(grade >=60){
            letter = "D";
            letterSignal= GetLetterSignal(grade);
            return (false, letter + letterSignal);
        }else{
            return (false, "F");
        }
    }

    static string GetLetterSignal(int grade){
        int remainder = grade % 10;
        if(remainder >= 7)
            return "+";
        else if (remainder >3)
            return "-";
        else
            return "";
    }
}