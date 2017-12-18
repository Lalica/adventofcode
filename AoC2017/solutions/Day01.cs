using System;
using System.IO;

namespace AoC2017.solutions
{
    class Day01
    {
        public static void Solution()
        {
            int sum1 = 0, sum2 = 0;
            string s;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,"inputs/input01.txt")))
            {
                s = sr.ReadLine();
            }
            Char[] inp = s.ToCharArray();
            for (int i = 0; i < inp.Length; i++)
            {
                if (inp[i].Equals(inp[(i + 1) % inp.Length]))
                {
                    sum1 += int.Parse(inp[i].ToString());
                }
                if (inp[i].Equals(inp[(inp.Length / 2 + i) % inp.Length]))
                {
                    sum2 += int.Parse(inp[i].ToString());
                }
            }
            Console.WriteLine("Part one: " + sum1);
            Console.WriteLine("Part two: " + sum2);
        }
    }
}
