using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AoC2017.solutions
{
    class Day06
    {
        public static void Solution()
        {
            int sum1 = 0, sum2 = 0;
            string[] temp;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName, "inputs/input06.txt")))
            {
                temp = sr.ReadLine().Split('\t');
            }
            int[] blocks = new int[temp.Length];
            int index = 0;
            foreach (string t in temp) //stvaram int array u kojem stavim sve brojeve iz inputa
            {
                blocks[index] = int.Parse(t);
                index++;
            }
            string toAdd = "";
            LinkedList<string> previousVariations = new LinkedList<string>(); //lista koju mjenjam (citav "progam" je jedan element) (string zbog lakseg printanja)
            foreach (int block in blocks) //prva varijacija (pocetan input) 
            {
                toAdd += block + " ";
            }
            previousVariations.AddLast(toAdd);
            int check = 0; //zastavica kad se dogodi loop
            while (check != 1)
            {
                toAdd = "";
                int max = 0;
                index = 0;
                for (int i = 0; i < blocks.Length; i++) //trazim najveci clan
                {
                    if (blocks[i] > max)
                    {
                        max = blocks[i];
                        index = i;
                    }
                }
                blocks[index] = 0; //postavljam najveci clan na nulu
                while (max > 0) //povecavam ostale clanove arraya za jedan
                {
                    blocks[(index + 1) % blocks.Length]++;
                    index++;
                    max--;
                }
                foreach (int block in blocks) //array pretvaram u string
                {
                    toAdd += block + " ";
                }
                sum1++;
                foreach (string variation in previousVariations) //provjeravam jel se dogodio loop
                {
                    if (variation.Equals(toAdd))
                    {
                        check = 1;
                        break;
                    }
                }
                previousVariations.AddLast(toAdd); //dodajem promjenjen "program" u listu
            }

            //drugi dio
            int last = 0;
            foreach (string variation in previousVariations)
            {
                if (variation.Equals(toAdd)) last++; //toAdd je zadnji clan, tj onaj od kojeg pocinje loop, on se nalazi 2 puta u listi
                if (last == 1) sum2++; //kad nade prvi put pocne brojati velicinu loopa
                if (last == 2) break; //kad nade drugi put prestaje brojati
            }
            Console.WriteLine("Part one: " + sum1);
            Console.WriteLine("Part two: " + sum2);
        }

        //Reddit rjesenje, prouciti i napisati bolje!!
        public static string PartOne(string input)
        {
            var words = input.Split(new string[] { "\t" }, StringSplitOptions.RemoveEmptyEntries);
            var banks = words.Select(x => int.Parse(x)).ToArray();
            var configs = new List<int[]>();

            while (!configs.Any(x => x.SequenceEqual(banks)))
            {
                configs.Add(banks.ToArray());
                RedistributeBlocks(banks);
            }

            return configs.Count().ToString();
        }

        private static void RedistributeBlocks(int[] banks)
        {
            var idx = banks.ToList().IndexOf(banks.Max());
            var blocks = banks[idx];

            banks[idx++] = 0;

            while (blocks > 0)
            {
                if (idx >= banks.Length)
                {
                    idx = 0;
                }

                banks[idx++]++;
                blocks--;
            }
        }

        public static string PartTwo(string input)
        {
            var words = input.Split(new string[] { "\t" }, StringSplitOptions.RemoveEmptyEntries);
            var banks = words.Select(x => int.Parse(x)).ToArray();
            var configs = new List<int[]>();

            while (!configs.Any(x => x.SequenceEqual(banks)))
            {
                configs.Add((int[])banks.Clone());
                RedistributeBlocks(banks);
            }

            var seenIndex = configs.IndexOf(configs.First(x => x.SequenceEqual(banks)));
            var steps = configs.Count() - seenIndex;

            return steps.ToString();
        }
    }
}
