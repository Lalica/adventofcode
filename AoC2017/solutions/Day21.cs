using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace AoC2017.solutions
{
    static class Day21
    {
        public static void Solution()
        {
            Dictionary<string, string> rules = new Dictionary<string, string>();
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input21.txt")))
            {
                string s;
                while ((s = sr.ReadLine()) != null)
                {
                    rules.Add(s.Split(new[] { " => " }, StringSplitOptions.RemoveEmptyEntries)[0],
                              s.Split(new[] { " => " }, StringSplitOptions.RemoveEmptyEntries)[1]);
                }
            }
            rules = AddRotations(rules);
            var picture = ".#./..#/###";
            int size = 3, part1 = 0;
            for (int i = 0; i < 18; i++)
            {
                picture = picture.Transform(rules);
                if (i == 4)
                {
                    part1 = picture.Count(c => c == '#');
                }
            }

            Console.WriteLine("Part one: " + part1);
            Console.WriteLine("Part two: " + picture.Count(c => c == '#'));
        }

        private static Dictionary<string, string> AddRotations(Dictionary<string, string> rules)
        {
            var copy = new Dictionary<string, string>(rules.Count * 5);
            foreach (var pair in rules)
            {
                string inputPic = pair.Key;
                copy[inputPic] = pair.Value;
                for (int i =0 ; i < 4; i++)
                {
                    inputPic = Symmetric(inputPic);
                    copy[inputPic] = pair.Value;

                    inputPic = Flip(inputPic);
                    copy[inputPic] = pair.Value;
                }
            }
            return copy;
        }

        private static string Symmetric(string m) =>
            m.Length == 11 ? $"{m[0]}{m[4]}{m[8]}/{m[1]}{m[5]}{m[9]}/{m[2]}{m[6]}{m[10]}" :
                $"{m[0]}{m[3]}/{m[1]}{m[4]}";

        private static string Flip(string m) =>
            m.Length == 11 ? $"{m[8]}{m[9]}{m[10]}/{m[4]}{m[5]}{m[6]}/{m[0]}{m[1]}{m[2]}" :
                $"{m[3]}{m[4]}/{m[0]}{m[1]}";

        private static string Transform(this string picture, Dictionary<string, string> rules) =>
            picture.BreakupPicture()
                .Select(g => rules[g])
                .JoinPictures();

        private static IEnumerable<string> BreakupPicture(this string picture)
        {
            string[] rows = picture.Split('/');
            int divisor = rows.Length % 2 == 0 ? 2 : 3;
            int numGroups = (int)Math.Pow(rows.Length / divisor, 2);
            int groupSize = rows.Length / divisor;
            for (int g = 0; g < numGroups; g++)
            {
                var sb = new StringBuilder();
                for (int y = 0; y < divisor; y++)
                {
                    for (int x = 0; x < divisor; x++)
                    {
                        sb.Append(rows[(g / groupSize) * divisor + y][(g % groupSize) * divisor + x]);
                    }
                    if (y != divisor - 1) sb.Append('/');
                }
                yield return sb.ToString();
            }
        }

        private static string JoinPictures(this IEnumerable<string> children)
        {
            string[][] groups = children.Select(s => s.Split('/')).ToArray();
            var divisor = groups[0][0].Length;
            var size = (int)Math.Sqrt(groups.Length * divisor * divisor);
            var sb = new StringBuilder();
            for (int y = 0; y < size; y++)
            {
                for (int x = 0; x < size; x++)
                {
                    sb.Append(groups[(y / divisor) * (size / divisor) + x / divisor][y % divisor][x % divisor]);
                }
                if (y != size - 1) sb.Append('/');
            }
            return sb.ToString();
        }
    }
}
