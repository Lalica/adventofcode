using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoC2017.solutions
{
    class Day11
    {
        public static void Solution()
        {
            List<string> layers;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input11.txt")))
            {
                layers = sr.ReadLine().Split(',').ToList();
            }

            int x = 0, y = 0, z = 0, sol = 0;
            foreach (var card in layers)
            {
                if (card == "n")
                {
                    y += 1;
                    z -= 1;
                }
                else if (card == "s")
                {
                    y -= 1;
                    z += 1;
                }
                else if (card == "ne")
                {
                    x += 1;
                    z -= 1;
                }
                else if (card == "sw")
                {
                    x -= 1;
                    z += 1;
                }
                else if (card == "nw")
                {
                    x -= 1;
                    y += 1;
                }
                else if (card == "se")
                {
                    x += 1;
                    y -= 1;
                }
                int dist = (Math.Abs(x) + Math.Abs(y) + Math.Abs(z)) / 2;
                sol = sol < dist ? dist : sol;
            }

            Console.WriteLine("Part one: " + (Math.Abs(x) + Math.Abs(y) + Math.Abs(z)) / 2);
            Console.WriteLine("Part two: " + sol);
        }
    }
}
