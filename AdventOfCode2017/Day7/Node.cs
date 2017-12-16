using System.Collections.Generic;

namespace Day7
{
    public class Node
    {
        public string name;
        public int weight;
        public LinkedList<string> above = new LinkedList<string>();

        public Node(string name, int weight, string[] above)
        {
            this.name = name;
            this.weight = weight;
            foreach (string a in above)
            {
                if (a == null) break;
                this.above.AddLast(a);
            }
        }
    }
}
