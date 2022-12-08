using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AoC2017.solutions
{
    class Day12
    {
        public static void Solution()
        {
            List<string> programs = new List<string>();
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input12.txt")))
            {
                string s;
                while ((s = sr.ReadLine()) != null)
                {
                    programs.Add(s);
                }
            }
            Dictionary<int, int[]> map = programs.Select((kv) => new { kv }).ToDictionary(pair => int.Parse(pair.kv.Replace(" <-> ", "|").Split('|').First()), pair => pair.kv.Replace(" <-> ", "|").Split('|').Last().Split(',').Select(x => int.Parse(x)).ToArray());
            HashSet<int> chain = new HashSet<int>(); chain.Clear();
            List<int[]> groups = new List<int[]>(); groups.Clear();
            foreach (int id in map.Keys)
                if (!groupExist(id))
                    groups.Add(groupByID(id));

            Console.WriteLine("Part one: " + groups.First(g => g.Contains(0)).Length);
            Console.WriteLine("Part two: " + groups.Count);

            int[] groupByID(int groupID)
            {
                int c = 0; chain.Clear(); chain.Add(groupID);
                while (c < chain.Count)
                {
                    foreach (int z in map[chain.ElementAt(c)]) { chain.Add(z); }
                    c++;
                }
                return chain.ToArray();
            }
            bool groupExist(int ID)
            {
                for (int i = 0; i < groups.Count; i++) { if (groups[i].Contains(ID)) { return true; } }
                return false;
            }
        }
    } 
}
