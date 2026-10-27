using System;

class Program
{
    static void Main()
    {
        string name;   
        float Khmer;
        float Math;
        float physics;
        float avg;

        Console.Write("Enter your name: ");
        name = Console.ReadLine();
        Console.WriteLine("Enter your Khmer score: ");
        Khmer = Convert.ToSingle(Console.ReadLine());
        Console.WriteLine("Enter your Math score: ");
        Math = Convert.ToSingle(Console.ReadLine());
        Console.WriteLine("Enter your Physics score: ");
        physics = Convert.ToSingle(Console.ReadLine());

        avg = (Khmer + Math + physics) / 3;
        if (avg >= 50)
        {
            Console.WriteLine($"Hello {name}, your average score is {avg:F2}. You passed the exam.");
        }
        else
        {
            Console.WriteLine($"Hello {name}, your average score is {avg:F2}. You failed the exam.");
        }
        
        
    }
}