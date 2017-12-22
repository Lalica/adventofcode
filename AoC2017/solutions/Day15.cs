using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoC2017.solutions
{
    class Day15
    {
        public static void Solution()
        {
            long firstA, firstB;
            int sum1=0, sum2 = 0;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input15.txt")))
            {
                string[] s = sr.ReadLine().Split(' ');
                firstA = long.Parse(s[s.Length - 1]);
                s = sr.ReadLine().Split(' ');
                firstB = long.Parse(s[s.Length - 1]);
            }

            long lastValueA = firstA, lastValueB = firstB;
            //for (int i = 0; i < 40000000; i++)
            //{
            //    lastValueA = (lastValueA * 16807) % 2147483647;
            //    lastValueB = (lastValueB * 48271) % 2147483647;
            //    string A = "0000000000000000" + Convert.ToString(lastValueA, 2);
            //    string B = "0000000000000000" + Convert.ToString(lastValueB, 2);
            //    if (A.Substring(A.Length - 16) == B.Substring(B.Length - 16))
            //    {
            //        sum1++;
            //    }
            //}

            lastValueA = firstA;
            lastValueB = firstB;
            List<string> A2 = new List<string>();
            List<string> B2 = new List<string>();
            int index = 0;
            for (int i = 0; i < 5000000; i++)
            {
                lastValueA = (lastValueA * 16807) % 2147483647;
                lastValueB = (lastValueB * 48271) % 2147483647;
                if(lastValueA % 4 == 0)
                {
                    A2.Add("0000000000000000" + Convert.ToString(lastValueA, 2));
                }
                if (lastValueB % 8 == 0)
                {
                    B2.Add("0000000000000000" + Convert.ToString(lastValueB, 2));
                }
                if (A2.Count > 0 && B2.Count > 0)
                {
                    if (A2.ToArray()[0].Substring(A2.ToArray()[0].Length - 16) ==
                        B2.ToArray()[0].Substring(B2.ToArray()[0].Length - 16))
                    {
                        sum2++;
                    }
                    A2.Remove(A2.ToArray()[0]);
                    B2.Remove(B2.ToArray()[0]);
                }
            }
            Console.WriteLine("Part one: " + sum1);
            Console.WriteLine("Part two: " + sum2);
        }
    }
}
