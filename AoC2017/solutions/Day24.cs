using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.IO;
using System.Linq;

namespace AoC2017.solutions
{
    class Day24
    {
        public static void Solution()
        {
            List<string> components = new List<string>();
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input24.txt")))
            {
                string s;
                while ((s = sr.ReadLine()) != null)
                {
                    components.Add(s);
                }
            }
            IImmutableList<(int, int)> edges = ImmutableList<(int, int)>.Empty;
            
            foreach (var line in components)
            {
                var nums = line.Split('/');
                edges = edges.Add((int.Parse(nums[0]), int.Parse(nums[1])));
            }
            (int, int) Search2(IImmutableList<(int, int)> e, int cur = 0, int strength = 0, int length = 0)
            {
                return e.Where(x => x.Item1 == cur || x.Item2 == cur).Select(x => Search2(e.Remove(x), x.Item1 == cur ? x.Item2 : x.Item1, strength + x.Item1 + x.Item2, length + 1)).Concat(Enumerable.Repeat((strength, length), 1)).OrderByDescending(x => x.Item2).ThenByDescending(x => x.Item1).First();
            } 

            Console.WriteLine("Part one: " + FindStrongest(components, 0, 0));
            //Console.WriteLine("Part two: " + FindLongest(components, 0, 0, 1)[1]);
            Console.WriteLine("Part two: " + Search2(edges).Item1);
        }

        private static int FindStrongest(List<string> components, int pin, int sum)
        {
            List<string> suitable = components.Where(s => int.Parse(s.Split('/')[0]) == pin || int.Parse(s.Split('/')[1]) == pin).ToList();
            List<int> sums = new List<int>();
            foreach (var suit in suitable)
            {
                components.Remove(suit);
                int newPin = int.Parse(suit.Split('/')[0]) == pin? int.Parse(suit.Split('/')[1]) : int.Parse(suit.Split('/')[0]);
                sums.Add(FindStrongest(components, newPin, int.Parse(suit.Split('/')[1]) + int.Parse(suit.Split('/')[0])));
                components.Add(suit);
            }

            return sum + (sums.Count > 0 ? sums.Max(): 0);
        }

        //private static int[] FindLongest(List<string> components, int pin, int sum, int lenght)
        //{
        //    List<string> suitable = components.Where(s => int.Parse(s.Split('/')[0]) == pin || int.Parse(s.Split('/')[1]) == pin).ToList();
        //    if (suitable.Count == 0)
        //    {
        //        return new[] {0, 0};
        //    }
        //    if (suitable.Count == 1)
        //    {
        //        int[] bridge = new int[2];
        //        bridge[0] = lenght +1;
        //        bridge[1] = sum + int.Parse(suitable.First().Split('/')[0]) + int.Parse(suitable.First().Split('/')[1]);
        //        return bridge;
        //    }
        //    List<int[]> sums = new List<int[]>();
        //    foreach (var suit in suitable)
        //    {
        //        sum += int.Parse(suit.Split('/')[1]) + int.Parse(suit.Split('/')[0]);
        //        components.Remove(suit);
        //        int newPin = int.Parse(suit.Split('/')[0]) == pin ? int.Parse(suit.Split('/')[1]) : int.Parse(suit.Split('/')[0]);
        //        int[] bridge = new int[2];
        //        bridge[0] = lenght + 1;
        //        bridge[1] = sum;
        //        sums.Add(bridge);
        //        sums.Add(FindLongest(components, newPin, sum, lenght+1));
        //        sum -= int.Parse(suit.Split('/')[1]) + int.Parse(suit.Split('/')[0]);
        //        components.Add(suit);
        //    }
        //
        //    int longest = sums.OrderBy(s => s[0]).Last()[0];
        //    return sums.Where(x => x[0] == longest).OrderBy(y => y[1]).Last();
        //}
    }
}
