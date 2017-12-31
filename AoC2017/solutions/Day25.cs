using System;
using System.Collections.Generic;
using System.IO;
using Microsoft.SqlServer.Server;

namespace AoC2017.solutions
{
    class Day25
    {
        public static void Solution()
        {
            string currentState;
            int steps;
            Dictionary<string, State> states = new Dictionary<string, State>();

            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input25.txt")))
            {
                currentState = sr.ReadLine().Split()[3].Remove(1);
                steps = int.Parse(sr.ReadLine().Split()[5]);

                string s, key=null;
                int i = 0;
                while ((s = sr.ReadLine()) != null)
                {
                    if (i % 10 == 0)
                    {
                        continue;
                    }
                    if (i % 10 == 1)
                    {
                        key = s.Split()[2].Remove(1);
                        states.Add(key, new State());
                    }
                    if (i % 10 == 3)
                    {
                        states[key].Write[0] = int.Parse(s.Split()[4].Remove(1));
                    }
                    if (i % 10 == 4)
                    {
                        states[key].Write[0] = int.Parse(s.Split()[4].Remove(1));
                    }
                    if (i % 10 == 2)
                    {

                    }
                    if (i % 10 == 2)
                    {

                    }
                    if (i % 10 == 2)
                    {

                    }
                    if (i % 10 == 2)
                    {

                    }
                }
            }
        }
    }

    class State
    {
        public int[] Write = new int[2];
        public bool[] Move = new bool[2];
        public string Cont;
    }
}
