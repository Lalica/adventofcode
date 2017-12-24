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

            int i = 0, j=0;
            string part1 = "";
            int part2 = 0;
            char currentDirection = 'd';
            bool check = false;
            while (j < path[0].Length)
            {
                if (path[0][j++] == '|')
                {
                    break;
                }
            }
            while (true)
            {
                if (check)
                {
                    break;
                }
                switch (currentDirection)
                {
                    case 'd':
                        while (path[i][j] != '+')
                        {
                            i++;
                            part2++;
                            if (path[i][j] >= 'A' && path[i][j] <= 'Z')
                            {
                                part1 += path[i][j];
                            }
                            if (path[i][j] == ' ')
                            {
                                check = true;
                                break;
                            }
                        }
                        if (check)
                        {
                            break;
                        }
                        part2++;
                        if (path[i][j + 1] == '-')
                        {
                            currentDirection = 'r';
                            j++;
                        }
                        else if (path[i][j - 1] == '-')
                        {
                            currentDirection = 'l';
                            j--;
                        }
                        continue;
                    case 'u':
                        while (path[i][j] != '+')
                        {
                            i--;
                            part2++;
                            if (path[i][j] >= 'A' && path[i][j] <= 'Z')
                            {
                                part1 += path[i][j];
                            }
                            if (path[i][j] == ' ')
                            {
                                check = true;
                                break;
                            }
                        }
                        if (check)
                        {
                            break;
                        }
                        part2++;
                        if (path[i][j + 1] == '-')
                        {
                            currentDirection = 'r';
                            j++;
                        }
                        else if (path[i][j - 1] == '-')
                        {
                            currentDirection = 'l';
                            j--;
                        }
                        continue;
                    case 'r':
                        while (path[i][j] != '+')
                        {
                            j++;
                            part2++;
                            if (path[i][j] >= 'A' && path[i][j] <= 'Z')
                            {
                                part1 += path[i][j];
                            }
                            if (path[i][j] == ' ')
                            {
                                check = true;
                                break;
                            }
                        }
                        if (check)
                        {
                            break;
                        }
                        part2++;
                        if (path[i+1][j] == '|')
                        {
                            currentDirection = 'd';
                            i++;
                        }
                        else if (path[i-1][j] == '|')
                        {
                            currentDirection = 'u';
                            i--;
                        }
                        continue;
                    case 'l':
                        while (path[i][j] != '+')
                        {
                            j--;
                            part2++;
                            if (path[i][j] >= 'A' && path[i][j] <= 'Z')
                            {
                                part1 += path[i][j];
                            }
                            if (path[i][j] == ' ')
                            {
                                check = true;
                                break;
                            }
                        }
                        if (check)
                        {
                            break;
                        }
                        part2++;
                        if (path[i + 1][j] == '|')
                        {
                            currentDirection = 'd';
                            i++;
                        }
                        else if (path[i - 1][j] == '|')
                        {
                            currentDirection = 'u';
                            i--;
                        }
                        continue;
                }
            }
            
            Console.WriteLine("Part one: " + part1);
            Console.WriteLine("Part two: " + part2);
        }
    }
}
