using System;
using System.IO;

namespace AoC2017.solutions
{
    class Day25
    {
        public static void Solution()
        {
            string[] instructions;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input25.txt")))
            {
                instructions = sr.ReadToEnd().Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries);
            }
        }
    }
}
