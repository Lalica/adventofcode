using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Day2
{
    public class Program
    {
        public static void Solution()
        {
            int sum1 = 0, sum2 = 0;
            using (StreamReader sr = File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName, "input2.txt")))
            {
                string s = "";
                char[] stringSeparators = { '\t' };
                while ((s = sr.ReadLine()) != null)
                {
                    string[] sizes = s.Split(stringSeparators, StringSplitOptions.RemoveEmptyEntries);

                    LinkedList<int> list = new LinkedList<int>();

                    for (int i = 0; i < sizes.Length; i++)
                    {
                        int b = int.Parse(sizes[i]);
                        list.AddLast(b);
                    }
                    int min = 0, max = 0, div = 0;
                    foreach (var num in list)
                    {
                        foreach (var num2 in list)
                        {
                            div = 0;
                            if (num % num2 == 0 && num2 != num)
                            {
                                div = num / num2;
                                break;
                            }
                        }
                        sum2 = sum2 + div;
                    }
                    min = list.Min();
                    max = list.Max();
                    sum1 += max - min;
                }
            }
            Console.WriteLine(sum1);
            Console.WriteLine(sum2);
            Console.Read();
        }
    }
}
