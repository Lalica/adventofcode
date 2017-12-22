using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoC2017.solutions
{
    class Day16
    {
        public static void Solution()
        {
            int sum1 = 0, sum2 = 0;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName, "inputs/input16.txt")))
            {
                string[] s = sr.ReadLine().Split(' ');
            }
        }
    }
}
