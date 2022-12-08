using System;
using System.Collections.Generic;
using System.IO;

namespace AoC2017.solutions
{
    class Day17
    {
        public static void Solution()
        {
            int s;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input17.txt")))
            {
                s = int.Parse(sr.ReadLine());
            }

            var spinlock = new List<int>() {0};
            int index = 0;
            for (int i = 1; i < 2018; i++)
            {
                index = (index + s) % i + 1;
                spinlock.Insert(index, i);
            }
            int part1 = spinlock[(index + 1) % spinlock.Count];

            index = 0;
            int part2=0;
            for (int i = 1; i < 50000000; i++)
            {
                index = (index + s) % i + 1;
                if (index == 1)
                {
                    part2 = i;
                }
            }

            Console.WriteLine("Part one: " + part1);
            Console.WriteLine("Part two: " + part2);
        }
    }
}
