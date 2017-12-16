using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Day7
{
    public class Program
    {
        public static void Solution()
        {
            string name1 = "NoName";
            int weight2=0;
            LinkedList<Node> tower = new LinkedList<Node>();
            using (StreamReader sr = File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName, "input7.txt")))
            {
                string s = "";
                string[] stringSeparators = {" ", "(" , ")", "->", ", "};
                string[] read;
                while ((s = sr.ReadLine()) != null)
                {
                    read = s.Split(stringSeparators, StringSplitOptions.RemoveEmptyEntries);
                    Node current = new Node(read[0], int.Parse(read[1]), read.Skip(2).ToArray());
                    tower.AddLast(current);
                }
            }

            foreach (Node t in tower)
            {
                int search = 0;
                string name = t.name;
                foreach (Node n in tower)
                {
                    if (n.above.Contains(name)) search = 1;
                }
                if (search == 0)
                {
                    name1 = name;
                    break;
                }
            }
            foreach (Node t in tower)
            {
                if (t.above.Count == 0) continue;
                int num = 0, sum=0;
                int[] all = new int[t.above.Count];
                foreach (string n in t.above)
                {
                    all[num] = findSumOfAbove(tower, tower.First(s => s.name.Equals(n))) + tower.First(s => s.name.Equals(n)).weight;
                    sum += all[num];
                    num++;
                }
                if (sum / num != all[0])
                {
                    int different = all.GroupBy( s => s).First(s => s.Count() == 1).Key;
                    int above = 0;
                    for (int i = 0; i < num; i++)
                    {
                        if (all[i] == different)
                        {
                            above = findSumOfAbove(tower, tower.First(s => s.name.Equals(t.above.ElementAt(i))));
                            weight2 = all[(i + 1) % all.Length] - above;
                            //break;
                        }
                    }
                }
            }

            Console.WriteLine(name1);
            Console.WriteLine(weight2);
            Console.Read();
        }

        public static int findSumOfAbove(LinkedList<Node> tower, Node node)
        {
            int sum = 0;
            foreach (string n in node.above)
            {
                int last = tower.First(s => s.name.Equals(n)).weight +
                           findSumOfAbove(tower, tower.First(s => s.name.Equals(n)));
                sum += last;
            }
            return sum;
        }
    }
}
