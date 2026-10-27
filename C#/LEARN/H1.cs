using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("gas Station");
        Console.WriteLine("sam buy gas for his car : ");
        double gasInTank = Convert.ToDouble(Console.ReadLine());

        if (gasInTank >= 35)
        {
            Console.WriteLine("You can refuel your car");
            double refuel = gasInTank *0.4/100;
            Console.WriteLine($"You can refuel {refuel:F2} liters of gas.");
        }
        else
        {
            Console.WriteLine("You cannot refuel your car");
        }
    }
}