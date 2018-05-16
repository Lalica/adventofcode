using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AoC2017.solutions
{
    internal class Day25
    {
        public static void Solution()
        {
            var transitions = new Dictionary<Tuple<string, int>, Tuple<string, int, string>>();

            using (var sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input25.txt")))
            {
                var currentState = sr.ReadLine().Split()[3].TrimEnd('.');
                var steps = int.Parse(sr.ReadLine().Split()[5]);
                var currentPosition = steps + 1;
                var tape = new int[steps * 2 + 1];

                string s;
                while ((s = sr.ReadLine()) != null)
                {
                    s = sr.ReadLine();
                    var newState = s.Split()[2].TrimEnd(':');
                    s = sr.ReadLine();
                    s = sr.ReadLine();
                    var nextSign = int.Parse(s.Trim().Split()[4].TrimEnd('.'));
                    s = sr.ReadLine();
                    var nextStep = s.Trim().Split()[6].TrimEnd('.');
                    s = sr.ReadLine();
                    var nextState = s.Trim().Split()[4].TrimEnd('.');
                    transitions[new Tuple<string, int>(newState, 0)] =
                        new Tuple<string, int, string>(nextState, nextSign, nextStep);
                    s = sr.ReadLine();
                    s = sr.ReadLine();
                    nextSign = int.Parse(s.Trim().Split()[4].TrimEnd('.'));
                    s = sr.ReadLine();
                    nextStep = s.Trim().Split()[6].TrimEnd('.');
                    s = sr.ReadLine();
                    nextState = s.Trim().Split()[4].TrimEnd('.');
                    transitions[new Tuple<string, int>(newState, 1)] =
                        new Tuple<string, int, string>(nextState, nextSign, nextStep);
                }

                TuringMachine(currentState, currentPosition, steps, tape, transitions);
                Console.Write("Part one: " + tape.Count(i => i == 1));
                Console.Write("Part two: " + "Merry Christmas!");
            }
        }

        public static void TuringMachine(string currentState, int currentPosition, int steps, int[] tape,
            Dictionary<Tuple<string, int>, Tuple<string, int, string>> transitions)
        {
            var currentTransition = new Tuple<string, int>(currentState, tape[currentPosition]);
            while (steps > 0)
            {
                var leftOrRight = transitions[currentTransition].Item3 == "right" ? 1 : -1;

                tape[currentPosition] = transitions[currentTransition].Item2;
                currentPosition = currentPosition + leftOrRight;
                currentState = transitions[currentTransition].Item1;

                currentTransition = new Tuple<string, int>(currentState, tape[currentPosition]);
                steps--;
            }
        }
    }
}