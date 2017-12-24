using System;
using System.IO;

namespace AoC2017.solutions
{
    class Day15
    {
        public static void Solution()
        {
            int firstA, firstB;
            int sum1=0, sum2 = 0;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input15.txt")))
            {
                string[] s = sr.ReadLine().Split(' ');
                firstA = int.Parse(s[s.Length - 1]);
                s = sr.ReadLine().Split(' ');
                firstB = int.Parse(s[s.Length - 1]);
            }
            int lastValueA = firstA, lastValueB = firstB;
            for (int i = 0; i < 40000000; i++)
            {
                lastValueA = Generator(16807, lastValueA);
                lastValueB = Generator(48271, lastValueB);
                if ((lastValueA & 0xFFFF) == (lastValueB & 0xFFFF))
                {
                    sum1++;
                }
            }

            lastValueA = firstA;
            lastValueB = firstB;
            for (int i = 0; i < 5000000; i++)
            {
                lastValueA = Generator(16807, lastValueA, 4);
                lastValueB = Generator(48271, lastValueB, 8);
                if ((lastValueA & 0xFFFF) == (lastValueB & 0xFFFF))
                {
                    sum2++;
                }
            }
            Console.WriteLine("Part one: " + sum1);
            Console.WriteLine("Part two: " + sum2);
        }

        private static int Generator(int cons, int prev, int mod = 1)
        {
            while (true)
            {
                prev = (int) (((long) prev * cons) % 2147483647);
                if (prev % mod == 0)
                {
                    return prev;
                }
            }
        }
    }
}
