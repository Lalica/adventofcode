using System;
using System.Collections.Generic;
using System.IO;
using System.Threading;

namespace AoC2017.solutions
{
    class Day18
    {
        public static void Solution()
        {
            string[] instructions;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input18.txt")))
            {
                instructions = sr.ReadToEnd().Split(new[] {'\r', '\n'}, StringSplitOptions.RemoveEmptyEntries);
            }

            long last = 0;
            long o1, o2=0, i=0;
            Dictionary<string, long> regs= new Dictionary<string, long>();
            while(i>-1 && i<instructions.Length)
            {
                if (!long.TryParse(instructions[i].Split(' ')[1], out o1))
                {
                    if (!regs.ContainsKey(instructions[i].Split(' ')[1]))
                    {
                        regs.Add(instructions[i].Split(' ')[1], 0);
                    }
                    o1 = regs[instructions[i].Split(' ')[1]];
                }
                if (instructions[i].Split(' ').Length > 2 && !long.TryParse(instructions[i].Split(' ')[2], out o2))
                {
                    if (!regs.ContainsKey(instructions[i].Split(' ')[2]))
                    {
                        regs.Add(instructions[i].Split(' ')[2], 0);
                    }
                    o2 = regs[instructions[i].Split(' ')[2]];
                }
                if (instructions[i].Split(' ')[0] == "snd")
                {
                    last = o1;
                }
                else if (instructions[i].Split(' ')[0] == "set")
                {
                    regs[instructions[i].Split(' ')[1]] = o2;
                }
                else if (instructions[i].Split(' ')[0] == "add")
                {
                    regs[instructions[i].Split(' ')[1]] += o2;
                }
                else if (instructions[i].Split(' ')[0] == "mul")
                {
                    regs[instructions[i].Split(' ')[1]] *= o2;
                }
                else if (instructions[i].Split(' ')[0] == "mod")
                {
                    regs[instructions[i].Split(' ')[1]] %= o2;
                }
                else if (instructions[i].Split(' ')[0] == "rcv")
                {
                    if (regs[instructions[i].Split(' ')[1]] != 0)
                    {
                        break;
                    }
                }
                else if (instructions[i].Split(' ')[0] == "jgz")
                {
                    if (o1 > 0)
                    {
                        i = i + o2 - 1;
                    }
                }
                i++;
            }
            List<long> queue0 = new List<long>();
            List<long> queue1 = new List<long>();
            new Thread(() =>
            {
                Thread.CurrentThread.IsBackground = true;
                Program(instructions, 0, queue1, queue0);
            }).Start();
            Program(instructions, 1, queue0, queue1);
            

            Console.WriteLine("Part one: " + last);
            Console.WriteLine("Part two: " + queue0.Count);
        }

        public static void Program(string[] instructions, int id, List<long> otherQueue, List<long> myQueue)
        {
            int last = 0;
            long o1, o2 = 0, i = 0;
            Dictionary<string, long> regs = new Dictionary<string, long>();
            while (i > -1 && i < instructions.Length)
            {
                if (!long.TryParse(instructions[i].Split(' ')[1], out o1))
                {
                    if (!regs.ContainsKey(instructions[i].Split(' ')[1]))
                    {
                        regs.Add(instructions[i].Split(' ')[1], instructions[i].Split(' ')[1] =="p" ? id : 0);
                    }
                    o1 = regs[instructions[i].Split(' ')[1]];
                }
                if (instructions[i].Split(' ').Length > 2 && !long.TryParse(instructions[i].Split(' ')[2], out o2))
                {
                    if (!regs.ContainsKey(instructions[i].Split(' ')[2]))
                    {
                        regs.Add(instructions[i].Split(' ')[2], 0);
                    }
                    o2 = regs[instructions[i].Split(' ')[2]];
                }
                if (instructions[i].Split(' ')[0] == "snd")
                {
                    otherQueue.Add(o1);
                }
                else if (instructions[i].Split(' ')[0] == "set")
                {
                    regs[instructions[i].Split(' ')[1]] = o2;
                }
                else if (instructions[i].Split(' ')[0] == "add")
                {
                    regs[instructions[i].Split(' ')[1]] += o2;
                }
                else if (instructions[i].Split(' ')[0] == "mul")
                {
                    regs[instructions[i].Split(' ')[1]] *= o2;
                }
                else if (instructions[i].Split(' ')[0] == "mod")
                {
                    regs[instructions[i].Split(' ')[1]] %= o2;
                }
                else if (instructions[i].Split(' ')[0] == "rcv")
                {
                    DateTime start = DateTime.Now;
                    while (myQueue.Count < last+1)
                    {
                        if ((DateTime.Now - start).Seconds > 20)
                        {
                            return;
                        }
                    }
                    regs[instructions[i].Split(' ')[1]] = myQueue[last];
                    last++;
                }
                else if (instructions[i].Split(' ')[0] == "jgz")
                {
                    if (o1 > 0)
                    {
                        i = i + o2 - 1;
                    }
                }
                i++;
            }
        }
    }
}
