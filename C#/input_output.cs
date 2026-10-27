using System;

class Program
{
    static void Main()
    {
        
        // output 
        Console.Write("Hello, World!"); // This line prints "Hello, World!" to the console
        Console.WriteLine("Hello, World!"); // This line prints "Hello, World!" to the console and moves to the next line

        // input

        string NAME;
        Console.Write("Enter your name: "); // This line prompts the user to enter their name
        NAME = Console.ReadLine(); // This line reads the user's input and stores it in the variable NAME
        Console.WriteLine($"Hello, {NAME}!"); // This line prints a greeting message that includes the user's name

        Console.Write("Enter your name: "); // This line prompts the user to enter their name   
        string name = Console.ReadLine();  
        Console.WriteLine($"Hello, {name}!");
        Console.



    }
}