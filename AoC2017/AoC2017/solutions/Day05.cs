using System;
using System.IO;

namespace AoC2017.solutions
{
    class Day05
    {
        public static void Solution()
        {
            int sum1 = 0, sum2 = 0;
            using (StreamReader sr = File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName, "inputs/input05.txt")))
            {
                string line;
                int[] steps1 = new int[10000];
                int[] steps2 = new int[10000];
                int i = 0;
                while ((line = sr.ReadLine()) != null)
                {
                    steps2[i] = steps1[i] = int.Parse(line);
                    i++;
                }
                int j = 0;
                while (j < i)
                {
                    int step = steps1[j];
                    steps1[j]++;
                    j += step;
                    sum1++;
                }

                j = 0;
                while (j < i)
                {
                    int step = steps2[j];
                    if (steps2[j] >= 3) steps2[j]--;
                    else steps2[j]++;
                    j += step;
                    sum2++;
                }
            }
            Console.WriteLine("Part one " + sum1);
            Console.WriteLine("Part two " + sum2);
        }
    }
}
