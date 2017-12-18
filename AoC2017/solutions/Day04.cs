using System;
using System.IO;
using System.Linq;

namespace AoC2017.solutions
{
    class Day04
    {
        public static void Solution()
        {
            int sum1 = 0, sum2 = 0;
            using (StreamReader sr = File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName, "inputs/input04.txt")))
            {
                string line;
                while ((line = sr.ReadLine()) != null)
                {
                    string[] words = line.Split(' ');
                    for (int i = 0; i < words.Length; i++)
                    {
                        int check = 0;
                        for (int j = i + 1; j < words.Length; j++)
                        {
                            if (words[i] == words[j])
                            {
                                check = 1;
                                break;
                            }
                        }
                        if (check == 1)
                        {
                            break;
                        }
                        if (i + 1 == words.Length)
                        {
                            sum1++;
                        }
                    }

                    for (int i = 0; i < words.Length; i++)
                    {
                        int check = 0;
                        for (int j = i + 1; j < words.Length; j++)
                        {
                            if (String.Concat(words[i].OrderBy(c => c)) == String.Concat(words[j].OrderBy(c => c)))
                            {
                                check = 1;
                                break;
                            }
                        }
                        if (check == 1)
                        {
                            break;
                        }
                        if (i + 1 == words.Length)
                        {
                            sum2++;
                        }
                    }
                }
            }
            Console.WriteLine("Part one " + sum1);
            Console.WriteLine("Part two " + sum2);
        }
    }
}
