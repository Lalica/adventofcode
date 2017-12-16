using System;
using System.IO;

namespace Day5
{
    public class Program
    {
        public static void Solution()
        {
            int sum1 = 0, sum2 = 0;
            using (StreamReader sr = File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName, "input5.txt")))
            {
                string line = "";
                int[] steps = new int[10000];
                int i = 0;
                while ((line = sr.ReadLine()) != null)
                {
                    steps[i] = int.Parse(line);
                    i++;
                }
                int j = 0;
                while (j < i)
                {
                    int step = steps[j];
                    steps[j]++;
                    j += step;
                    sum1++;
                }
            }
            using (StreamReader sr = File.OpenText("C: /Users/laura/source/repos/AdventOfCode2017/Day5/input.txt"))
            {
                string line = "";
                int[] steps = new int[10000];
                int i = 0;
                while ((line = sr.ReadLine()) != null)
                {
                    steps[i] = int.Parse(line);
                    i++;
                }
                int j = 0;
                while (j < i)
                {
                    int step = steps[j];
                    if (steps[j] >= 3) steps[j]--;
                    else steps[j]++;
                    j += step;
                    sum2++;
                }
            }
            Console.WriteLine(sum1);
            Console.WriteLine(sum2);
            Console.Read();
        }
    }
}
