using System;
using System.Collections.Generic;
using System.IO;

namespace AoC2017.solutions
{
    class Day23
    {
        public static void Solution()
        {
            string[] instructions;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input23.txt")))
            {
                instructions = sr.ReadToEnd().Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries);
            }

            //Part1
            int sum1 = 0;
            long o1, o2 = 0, i = 0;
            Dictionary<string, long> regs = new Dictionary<string, long> { { "a", 0 }, { "b", 0 }, { "c", 0 }, { "d", 0 },
                                                                           { "e", 0 }, { "f", 0 }, { "g", 0 }, { "h", 0 } };
            while (i > -1 && i < instructions.Length)
            {
                if (!long.TryParse(instructions[i].Split(' ')[1], out o1))
                {
                    o1 = regs[instructions[i].Split(' ')[1]];
                }
                if (instructions[i].Split(' ').Length > 2 && !long.TryParse(instructions[i].Split(' ')[2], out o2))
                {
                    o2 = regs[instructions[i].Split(' ')[2]];
                }
                i++;
                switch (instructions[i - 1].Split(' ')[0])
                {
                    case "set":
                        regs[instructions[i - 1].Split(' ')[1]] = o2;
                        continue;
                    case "sub":
                        regs[instructions[i - 1].Split(' ')[1]] -= o2;
                        continue;
                    case "mul":
                        regs[instructions[i - 1].Split(' ')[1]] *= o2;
                        sum1++;
                        continue;
                    case "jnz":
                        if (o1 != 0)
                        {
                            i = i + o2 - 1;
                        }
                        continue;
                }
            }

            //Part2
            int a = 1, d, f, g, h=0;
            int b = int.Parse(instructions[0].Split(' ')[2]);
            b *= 100;
            b += 100000;
            int c = b;
            c += 17000;
            do
            {
                f = 1;
                for (d = 2; d < b; d++)
                {
                    if (b % d == 0)
                    {
                        f = 0;
                        break;
                    }
                }
                if (f == 0)
                {
                    h++;
                }
                g = b - c;
                b += 17;
            } while (g != 0);

            Console.WriteLine("Part one: " + sum1);
            Console.WriteLine("Part two: " + h);
        }
    }
}
