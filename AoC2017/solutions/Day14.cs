using System;
using System.IO;

namespace AoC2017.solutions
{
    class Day14
    {
        public static void Solution()
        {
            string s;
            using (StreamReader sr = File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName, "inputs/input14.txt")))
            {
                s = sr.ReadLine();
            }

            int sum1 = 0, index =0;
            string[] map = new string[128];
            for (int i = 0; i < 128; i++)
            {
                string knotHash = Day10.KnotHash(s + "-" + i);
                string row = "";
                foreach (var hex in knotHash)
                {
                    row += Convert.ToString(Convert.ToByte(hex.ToString(), 16), 2).PadLeft(4, '0');
                }
                map[index++] = row;
                foreach (var bin in row)
                {
                    sum1 += int.Parse(bin.ToString());
                }
            }
            
            bool[,] visited = new bool[128, 128];
            int sum2 = 0;

            for (int y = 0; y < visited.GetLength(1); y++)
            {
                for (int x = 0; x < visited.GetLength(0); x++)
                {
                    if (visited[x, y] || map[x][y] == '0')
                    {
                        continue;
                    }

                    Visit(x, y, map, visited);
                    sum2++;
                }
            }

            Console.WriteLine("Part one: " + sum1);
            Console.WriteLine("Part two: " + sum2);
        }

        private static void Visit(int x, int y, string[] input, bool[,] visited)
        {
            if (visited[x, y])
            {
                return;
            }
            visited[x, y] = true;
            if (input[x][y] == '0')
            {
                return;
            }
            if (x > 0) Visit(x - 1, y, input, visited);
            if (x < 127) Visit(x + 1, y, input, visited);
            if (y > 0) Visit(x, y - 1, input, visited);
            if (y < 127) Visit(x, y + 1, input, visited);
        }
    }
}
