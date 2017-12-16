using System;
using System.Collections.Generic;

namespace Day3
{
    public class Program
    {
        public static void Solution()
        {
            int input = 361527;
            int last1, sum1 = 0;

            for (last1 = 3; last1 < input; last1 += 2)
            {
                if (last1 * last1 > input) break;
            }
            last1 *= last1;

            for (int k = 301; k >= -301; k--)
            {
                int check = 0;
                for (int j = 301; j >= -301; j--)
                {
                    if (last1 == input)
                    {
                        sum1 = k + j;
                        check = 1;
                        break;
                    }
                    last1--;
                }
                if (check == 1) break;
            }
            Console.WriteLine(sum1);

            Dictionary<Tuple<int, int>, int> spiral = new Dictionary<Tuple<int, int>, int>();
            spiral.Add(new Tuple<int, int>(0, 0), 1);
            int lastValue = 1, step = 1, sideCounter = 1;
            Tuple<int, int> currentPlacement = new Tuple<int, int>(0, 0);
            string side = "right";
            while (lastValue < input)
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

                        lastValue = CalculateNextValue(spiral, currentPlacement);
                        spiral.Add(currentPlacement, lastValue);
                        if (lastValue > input)
                        {
                            /* Prints all numbers in the spiral
                            foreach (Tuple<int, int> key in spiral.Keys)
                            {
                                Console.WriteLine(key + " " + spiral[key]);
                            }
                            */
                            Console.WriteLine(lastValue);
                            Console.Read();
                        }
                    }
                    side = nextSide(sideCounter);
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

        public static string nextSide(int index)
        {
            string[] sides = { "right", "up", "left", "down" };
            return sides[index % sides.Length];
        }
    }
}