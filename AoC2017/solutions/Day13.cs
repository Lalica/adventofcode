using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AoC2017.solutions
{
    class Day13
    {
        public static void Solution()
        {
            Dictionary<int, int> layers = new Dictionary<int, int>();
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input13.txt")))
            {
                string s;
                while ((s = sr.ReadLine()) != null)
                {
                    layers.Add(int.Parse(s.Split(':')[0]), int.Parse(s.Split(':')[1]));
                }
            }

            int sum1 = 0;
            for (int i = 1; i <= layers.Keys.Max(); i++)
            {
                if (!layers.ContainsKey(i))
                {
                    continue;
                }

                if ((i) % (layers[i] * 2 - 2) == 0)
                {
                    sum1 += i * layers[i];
                }
            }

            int j=1;
            while (true)
            {
                bool check = true;
                for (int i = 0; i <= layers.Keys.Max(); i++)
                {
                    if (!layers.ContainsKey(i))
                    {
                        continue;
                    }
            
                    if ((i + j) % (layers[i] * 2 - 2) == 0)
                    {
                        check = false;
                        break;
                    }
                }
                if (check)
                {
                    break;
                }
                j++;
            }

            Console.WriteLine("Part one: " + sum1);
            Console.WriteLine("Part two : " + j);
        }
    }
}
