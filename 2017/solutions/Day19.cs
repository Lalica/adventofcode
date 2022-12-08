using System;
using System.IO;

namespace AoC2017.solutions
{
    class Day19
    {
        public static void Solution()
        {
            string[] path;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input19.txt")))
            {
                path = sr.ReadToEnd().Split('\n');
            }

            int i = 1, part2 = 1, j = path[0].IndexOf("|");
            string part1 = "";
            char currentDirection = 'd';
            while (true)
            {
                if (path[i][j] == ' ')
                {
                    break;
                }
                part2++;
                if (char.IsLetter(path[i][j]))
                {
                    part1 += path[i][j];
                }
                if (path[i][j] == '+')
                {
                    if (currentDirection == 'd' || currentDirection == 'u')
                    {
                        currentDirection = path[i][j + 1] == '-' ? 'r' : 'l';
                        j = j + (path[i][j + 1] == '-' ? 1 : -1);
                    }
                    else
                    {
                        currentDirection = path[i + 1][j] == '|' ? 'd' : 'u';
                        i = i + (path[i + 1][j] == '|' ? 1 : -1);
                    }
                    part2++;
                }
                switch (currentDirection)
                {
                    case 'd':
                        i++;
                        continue;
                    case 'u':
                        i--;
                        continue;
                    case 'r':
                        j++;
                        continue;
                    case 'l':
                        j--;
                        continue;
                }
            }
            Console.WriteLine("Part one: " + part1);
            Console.WriteLine("Part two: " + part2);
        }
    }
}

//Really cool reddit solution:
//var map = GetDay(19);
//var word = "";
//var steps = 0;
//Complex i = Complex.ImaginaryOne, pos = new Complex(0, map.First().IndexOf("|")), dir = new Complex(1, 0); // down
//while (true)
//{
//  var itm = map[(int)pos.Real][(int)pos.Imaginary];
//  if (itm == '+') dir *= (map[(int)(pos + dir * i).Real][(int)(pos + dir * i).Imaginary] != ' ') ? i : -i;
//  else if (char.IsLetter(itm)) word += itm;
//  else if (itm == ' ') break;
//  pos += dir;
//  steps++;
//}
//Console.WriteLine($"Part 1: {word}\nPart 2: {steps}");
