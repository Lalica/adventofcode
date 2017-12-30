using System;
using System.IO;

namespace AoC2017.solutions
{
    class Day22
    {
        public static void Solution()
        {
            string[] map;
            string s;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input22.txt")))
            {
                s = sr.ReadToEnd();
            }
            //Part1
            map = s.Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries);
            int currentI = map.Length / 2, currentJ = map[0].Length /2, sum1 = 0;
            int currentDirection = 0; // up = 0, right = 1, down = 2, left = 3
            for (int i = 0; i < 10000; i++)
            {
                if (currentI == map.Length || currentJ == map.Length || currentI == -1 || currentJ == -1)
                {
                    map = ResizeMap(map);
                    currentI++;
                    currentJ++;
                }
                if (map[currentI][currentJ] == '#')
                {
                    currentDirection = (currentDirection + 1) % 4;
                    map[currentI] = map[currentI].Substring(0, currentJ)+"."+ map[currentI].Substring(currentJ + 1);
                }
                else
                {
                    currentDirection = (currentDirection + 3) % 4;
                    map[currentI] = map[currentI].Substring(0, currentJ) + "#" + map[currentI].Substring(currentJ + 1);
                    sum1++;
                }
                switch (currentDirection)
                {
                    case 0:
                        currentI--;
                        continue;
                    case 1:
                        currentJ++;
                        continue;
                    case 2:
                        currentI++;
                        continue;
                    case 3:
                        currentJ--;
                        continue;
                }
            }

            //Part2
            map = s.Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries);
            bool[,] flags = new bool[map.Length, map[0].Length];
            currentI = map.Length / 2; currentJ = map[0].Length / 2;
            int sum2 = 0; currentDirection = 0; // up = 0, right = 1, down = 2, left = 3
            for (int i = 0; i < 10000000; i++)
            {
                if (currentI == map.Length || currentJ == map.Length || currentI == -1 || currentJ == -1)
                {
                    map = ResizeMap(map);
                    flags = ResizeFlags(flags);
                    currentI++;
                    currentJ++;
                }
                if (map[currentI][currentJ] == '#')
                {
                    if (flags[currentI, currentJ])
                    {
                        currentDirection = (currentDirection + 2) % 4;
                        map[currentI] = map[currentI].Substring(0, currentJ) + "." + map[currentI].Substring(currentJ + 1);
                        flags[currentI, currentJ] = false;
                    }
                    else
                    {
                        currentDirection = (currentDirection + 1) % 4;
                        flags[currentI, currentJ] = true;
                    }
                }
                else
                {
                    if (flags[currentI, currentJ])
                    {
                        map[currentI] = map[currentI].Substring(0, currentJ) + "#" + map[currentI].Substring(currentJ + 1);
                        flags[currentI, currentJ] = false;
                        sum2++;
                    }
                    else
                    {
                        currentDirection = (currentDirection + 3) % 4;
                        flags[currentI, currentJ] = true;
                    }
                    
                }
                switch (currentDirection)
                {
                    case 0:
                        currentI--;
                        continue;
                    case 1:
                        currentJ++;
                        continue;
                    case 2:
                        currentI++;
                        continue;
                    case 3:
                        currentJ--;
                        continue;
                }
            }

            Console.WriteLine("Part one: " + sum1);
            Console.WriteLine("Part two: " + sum2);
        }

        private static string[] ResizeMap(string[] map)
        {
            string[] copy = new string[map.Length+2];
            copy[0] = copy[copy.Length - 1] = "";
            for (int i = 0; i < map[0].Length+2; i++)
            {
                copy[0] += ".";
                copy[copy.Length - 1] += ".";
            }
            for (int i = 0; i < map.Length; i++)
            {
                copy[i+1] = "." + map[i] + ".";
            }
            return copy;
        }

        private static bool[,] ResizeFlags(bool[,] flags)
        {
            bool[,] copy = new bool[(int)Math.Sqrt(flags.Length) + 2, (int)Math.Sqrt(flags.Length) + 2];
            for (int i = 1; i < (int)Math.Sqrt(flags.Length) + 1; i++)
            {
                for (int j = 1; j < (int) Math.Sqrt(flags.Length) + 1; j++)
                {
                    copy[i,j] = flags[i-1,j-1];
                }
            }
            return copy;
        }
    }
}
