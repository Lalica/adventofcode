using System;
using System.IO;

namespace AoC2017.solutions
{
    class Day10
    {
        public static void Solution()
        {
            string s;
            using (StreamReader sr = File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName, "inputs/input10.txt")))
            {
                s = sr.ReadLine();
            }

            //Part1
            string[] lenghts = s.Split(',');
            int skipSize = 0, currentPosition = 0; ;
            int[] list = new int[256];
            for (int i = 0; i < list.Length; i++)
            {
                list[i] = i;
            }

            foreach (string l in lenghts)
            {
                int j = int.Parse(l) + currentPosition - 1;
                for (int i = currentPosition; i <= int.Parse(l) / 2 + currentPosition - 1; i++)
                {
                    int help = list[i % list.Length];
                    list[i % list.Length] = list[j % list.Length];
                    list[j % list.Length] = help;
                    j--;
                }
                currentPosition += int.Parse(l) + skipSize;
                skipSize++;
            }
            int sum1 = list[0] * list[1];

            Console.WriteLine("Part one: " + sum1);
            Console.WriteLine("Part two: " + KnotHash(s));
        }

        public static string KnotHash(string s)
        {
            char[] chars = s.ToCharArray();
            int[] lenghts2 = new int[chars.Length + 5];
            int skipSize2 = 0, currentPosition2 = 0;
            int[] list2 = new int[256];
            for (int i = 0; i < list2.Length; i++)
            {
                list2[i] = i;
            }
            for (int i = 0; i < chars.Length; i++)
            {
                lenghts2[i] = chars[i];
            }
            lenghts2[chars.Length] = 17;
            lenghts2[chars.Length + 1] = 31;
            lenghts2[chars.Length + 2] = 73;
            lenghts2[chars.Length + 3] = 47;
            lenghts2[chars.Length + 4] = 23;

            for (int n = 0; n < 64; n++)
            {
                foreach (int l in lenghts2)
                {
                    int j = l + currentPosition2 - 1;
                    for (int i = currentPosition2; i <= l / 2 + currentPosition2 - 1; i++)
                    {
                        int help = list2[i % list2.Length];
                        list2[i % list2.Length] = list2[j % list2.Length];
                        list2[j % list2.Length] = help;
                        j--;
                    }
                    currentPosition2 += l + skipSize2;
                    skipSize2++;
                }
            }
            string denseHash = "";
            for (int i = 0; i < 16; i++)
            {
                int num = 0;
                for (int j = 0; j < 16; j++)
                {
                    num = num ^ list2[j + 16 * i];
                }
                denseHash += num.ToString("X2");
            }
            return denseHash.ToLower();
        }
    }
}
