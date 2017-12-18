using System;
using System.Collections.Generic;
using System.IO;

namespace AoC2017.solutions
{
    class Day03
    {
        public static void Solution()
        {
            string s;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,"inputs/input03.txt")))
            {
                s = sr.ReadLine();
            }

            //Part one
            int lastValue = 1;
            int counter = 0;
            int sideLength = 3;
            while (lastValue < int.Parse(s))
            {
                lastValue = sideLength * sideLength;
                counter++;
                sideLength += 2;
            }
            sideLength -= 2;
            int sum1 = (sideLength - 1) / 2 - (int.Parse(s) - (lastValue - sideLength + 1)) + counter;
            Console.WriteLine("Part one: " + sum1);

            //Part two
            Dictionary<Tuple<int, int>, int> spiral = new Dictionary<Tuple<int, int>, int> {{new Tuple<int, int>(0, 0), 1}};
            int lastValue2 = 1, step = 1, sideCounter = 1;
            Tuple<int, int> currentPlacement = new Tuple<int, int>(0, 0);
            string side = "right";
            while (lastValue2 < int.Parse(s))
            {
                for (int i = 0; i < 2; i++)
                {
                    for (int j = 0; j < step; j++)
                    {
                        switch (side)
                        {
                            case "right":
                                currentPlacement = new Tuple<int, int>(currentPlacement.Item1 + 1, currentPlacement.Item2);
                                break;
                            case "up":
                                currentPlacement = new Tuple<int, int>(currentPlacement.Item1, currentPlacement.Item2 + 1);
                                break;
                            case "left":
                                currentPlacement = new Tuple<int, int>(currentPlacement.Item1 - 1, currentPlacement.Item2);
                                break;
                            case "down":
                                currentPlacement = new Tuple<int, int>(currentPlacement.Item1, currentPlacement.Item2 - 1);
                                break;
                        }

                        lastValue2 = CalculateNextValue(spiral, currentPlacement);
                        spiral.Add(currentPlacement, lastValue2);
                        if (lastValue2 > int.Parse(s))
                        {
                            Console.WriteLine("Part two: " + lastValue2);
                            return;
                        }
                    }
                    side = NextSide(sideCounter);
                    sideCounter++;
                }
                step += 1;
            }
        }

        public static int CalculateNextValue(Dictionary<Tuple<int, int>, int> spiral, Tuple<int, int> currentPlacement)
        {
            int nextValue = 0;

            LinkedList<Tuple<int, int>> keys = new LinkedList<Tuple<int, int>>();
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1 + 1, currentPlacement.Item2 + 1));
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1 + 1, currentPlacement.Item2));
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1 + 1, currentPlacement.Item2 - 1));
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1, currentPlacement.Item2 + 1));
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1, currentPlacement.Item2 - 1));
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1 - 1, currentPlacement.Item2 + 1));
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1 - 1, currentPlacement.Item2));
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1 - 1, currentPlacement.Item2 - 1));

            foreach (Tuple<int, int> key in keys)
            {
                if (spiral.ContainsKey(key))
                {
                    nextValue += spiral[key];
                }
            }
            return nextValue;
        }

        public static string NextSide(int index)
        {
            string[] sides = { "right", "up", "left", "down" };
            return sides[index % sides.Length];
        }
    }
}
