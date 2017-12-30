using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoC2017.solutions
{
    class Day11
    {
        public static void Solution()
        {
            List<string> layers;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input11.txt")))
            {
                layers = sr.ReadLine().Split(',').ToList();
            }
            
        }
    }
}
