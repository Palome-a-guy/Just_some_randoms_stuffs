using System;

namespace Basic
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Number :");
            string? num = Console.ReadLine();

            if (num == "1")
            {
                bool test = true;

                if (test == true)
                {
                    string name = "Wow tu as eu le bon nombre (test en utilisant bool)";
                    Console.WriteLine(name);
                }
            } 
        }
    }
} 