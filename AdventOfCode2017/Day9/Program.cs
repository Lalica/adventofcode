using System;
using System.IO;

namespace Day9
{
    public class Program
    {
        public static void Solution()
        {
            int sum1 = 0, sum2=0;
            char[] stream;
            using (StreamReader sr = File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName, "input9.txt")))
            {
                stream = sr.ReadToEnd().ToCharArray();
            }

            int numOfOpenGroups = 0;
            bool garbageOpen = false;
            for (int i=0; i < stream.Length; i++)
            {
                if (stream[i].Equals('!') && garbageOpen) i++;
                else if (stream[i].Equals('>')) garbageOpen = false;
                else if (garbageOpen) sum2++;
                else if (stream[i].Equals('<')) garbageOpen = true;
                else if (stream[i].Equals('{'))
                {
                    numOfOpenGroups++;
                    sum1 += numOfOpenGroups;
                }
                else if (stream[i].Equals('}')) numOfOpenGroups--;
            }
            Console.WriteLine(sum1);
            Console.WriteLine(sum2);
            Console.Read();
        }
    }
}
