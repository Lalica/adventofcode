using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace AoC2017.solutions
{
    class Day16
    {
        public static void Solution()
        {
            string[] s;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName, "inputs/input16.txt")))
            {
                s = sr.ReadLine().Split(',');
            }
            string[] initial = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"};
            List<string> programs = initial.ToList();
            
            //Part1
            Dance(programs, s);
            string part1= String.Join("", programs.ToArray());

            //Part2
            programs = initial.ToList();
            int i = 0;
            while (true)
            {
                i++;
                Dance(programs,s);
                if (Enumerable.SequenceEqual(initial.ToList(), programs))
                {
                    break;
                }
            }
            programs = initial.ToList();
            for (int j = 0; j < 1000000000%i; j++)
            {
                Dance(programs, s);
            }

            Console.WriteLine("Part one: " + part1);
            Console.WriteLine("Part two: " + String.Join("", programs.ToArray()));
        }

        private static void Dance(List<string> programs, string[] moves)
        {
            foreach (var o in moves)
            {
                if (o.ToArray()[0] == 's')
                {
                    List<string> temp = programs.Where(p => programs.IndexOf(p) >= programs.Count - int.Parse(o.Substring(1))).ToList();
                    temp.Reverse();
                    programs.RemoveRange(programs.Count - int.Parse(o.Substring(1)), temp.Count);
                    foreach (var t in temp)
                    {
                        programs.Insert(0, t);
                    }
                }
                else if (o.ToArray()[0] == 'x')
                {
                    string temp = programs[int.Parse(o.Substring(1).Split('/')[0])];
                    programs[int.Parse(o.Substring(1).Split('/')[0])] = programs[int.Parse(o.Substring(1).Split('/')[1])];
                    programs[int.Parse(o.Substring(1).Split('/')[1])] = temp;
                }
                else if (o.ToArray()[0] == 'p')
                {
                    int indexA = programs.IndexOf(o.Substring(1).Split('/')[0]);
                    int indexB = programs.IndexOf(o.Substring(1).Split('/')[1]);
                    string temp = programs[indexA];
                    programs[indexA] = programs[indexB];
                    programs[indexB] = temp;
                }
            }
        }
    }
}
