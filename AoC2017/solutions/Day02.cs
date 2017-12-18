using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AoC2017.solutions
{
    class Day02
    {
        public static void Solution()
        {
            int sum1 = 0, sum2 = 0;
            string s;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName, "inputs/input02.txt")))
            {
                while ((s = sr.ReadLine()) != null)
                {
                    string[] sizes = s.Split('\t');
                    LinkedList<int> list = new LinkedList<int>();
                    for (int i = 0; i < sizes.Length; i++)
                    {
                        list.AddLast(int.Parse(sizes[i]));
                    }
                    int min = 0, max = 0, div = 0;
                    foreach (var num in list)
                    {
                        foreach (var num2 in list)
                        {
                            div = 0;
                            if (num % num2 == 0 && num2 != num)
                            {
                                div = num / num2;
                                break;
                            }
                        }
                        sum2 = sum2 + div;
                    }
                    min = list.Min();
                    max = list.Max();
                    sum1 += max - min;
                }
            }
            Console.WriteLine("Part one: " + sum1);
            Console.WriteLine("Part two: " + sum2);
        }
    }
}
