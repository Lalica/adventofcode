using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AoC2017.solutions
{
    class Day08
    {
        public static void Solution()
        {
            int max1, max2 = 0;
            LinkedList<Instruction> instructions = new LinkedList<Instruction>();
            Dictionary<String, int> registers = new Dictionary<string, int>();
            using (StreamReader sr = File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName, "inputs/input08.txt")))
            {
                string s;
                string[] stringSeparators = { " " };
                string[] read;
                while ((s = sr.ReadLine()) != null)
                {
                    read = s.Split(stringSeparators, StringSplitOptions.RemoveEmptyEntries);
                    instructions.AddLast(new Instruction(read[0], read[1], int.Parse(read[2]), read[4], read[5],
                        int.Parse(read[6])));
                    if (!registers.ContainsKey(read[0])) registers.Add(read[0], 0);
                }

                foreach (Instruction i in instructions)
                {
                    if (i.con.Equals(">"))
                    {
                        if (registers[i.conReg] > i.conValue)
                        {
                            if (i.iOrD.Equals("inc")) registers[i.reg] += i.value;
                            else registers[i.reg] -= i.value;
                        }
                    }
                    if (i.con.Equals(">="))
                    {
                        if (registers[i.conReg] >= i.conValue)
                        {
                            if (i.iOrD.Equals("inc")) registers[i.reg] += i.value;
                            else registers[i.reg] -= i.value;
                        }
                    }
                    if (i.con.Equals("<"))
                    {
                        if (registers[i.conReg] < i.conValue)
                        {
                            if (i.iOrD.Equals("inc")) registers[i.reg] += i.value;
                            else registers[i.reg] -= i.value;
                        }
                    }
                    if (i.con.Equals("<="))
                    {
                        if (registers[i.conReg] <= i.conValue)
                        {
                            if (i.iOrD.Equals("inc")) registers[i.reg] += i.value;
                            else registers[i.reg] -= i.value;
                        }
                    }
                    if (i.con.Equals("=="))
                    {
                        if (registers[i.conReg] == i.conValue)
                        {
                            if (i.iOrD.Equals("inc")) registers[i.reg] += i.value;
                            else registers[i.reg] -= i.value;
                        }
                    }
                    if (i.con.Equals("!="))
                    {
                        if (registers[i.conReg] != i.conValue)
                        {
                            if (i.iOrD.Equals("inc")) registers[i.reg] += i.value;
                            else registers[i.reg] -= i.value;
                        }
                    }
                    if (registers.Values.Max() > max2) max2 = registers.Values.Max();
                }
                max1 = registers.Values.Max();
                Console.WriteLine("Part one: " + max1);
                Console.WriteLine("Part two: " + max2);
            }
        }
    }

    public class Instruction
    {
        public String reg;
        public String iOrD;
        public int value;
        public String conReg;
        public String con;
        public int conValue;

        public Instruction(String reg, String iOrD, int value, String conReg, String con, int conValue)
        {
            this.con = con;
            this.conReg = conReg;
            this.conValue = conValue;
            this.iOrD = iOrD;
            this.reg = reg;
            this.value = value;
        }
    }
}
