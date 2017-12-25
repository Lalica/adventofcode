using System.IO;

namespace AoC2017.solutions
{
    class Day21
    {
        public static void Solution()
        {
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input21.txt")))
            {
                string s;
                while ((s = sr.ReadLine()) != null)
                {
                }
            }
        }
    }
}
