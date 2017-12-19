using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AoC2017.solutions
{
    class Day06
    {
        public static void Solution()
        {
            string[] temp;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName, "inputs/input06.txt")))
            {
                temp = sr.ReadLine().Split('\t');
            }
            int[] blocks = temp.Select(x => int.Parse(x)).ToArray();
            List<int[]> previousVariations = new List<int[]>();
            while (!previousVariations.Any(x => x.SequenceEqual(blocks)))
            {
                previousVariations.Add(blocks.ToArray());
                RedistributeBlocks(blocks);
            }

            //Part one
            int sum1 = previousVariations.Count;
            //Part two
            int seenIndex = previousVariations.IndexOf(previousVariations.First(x => x.SequenceEqual(blocks)));
            int steps = previousVariations.Count - seenIndex;
            int sum2 = steps;

            Console.WriteLine("Part one: " + sum1);
            Console.WriteLine("Part two: " + sum2);
        }

        private static void RedistributeBlocks(int[] blocks)
        {
            var idx = blocks.ToList().IndexOf(blocks.Max());
            var newBlocks = blocks[idx];

            blocks[idx++] = 0;

            while (newBlocks > 0)
            {
                if (idx >= blocks.Length)
                {
                    idx = 0;
                }

                blocks[idx++]++;
                newBlocks--;
            }
        }
    }
}
