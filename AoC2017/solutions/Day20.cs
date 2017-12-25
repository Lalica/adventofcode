using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AoC2017.solutions
{
    class Day20
    {
        public static void Solution()
        {
            Dictionary<int, int> particles = new Dictionary<int, int>();
            List<Particle> remains = new List<Particle>();
            int index = 0;
            using (StreamReader sr =
                File.OpenText(Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()).Parent.FullName,
                    "inputs/input20.txt")))
            {
                string s;
                while ((s = sr.ReadLine()) != null)
                {
                    string[] cp = s.Split(new [] {"p=<", ",", ">, v=<", ">, a=<", ">"},
                        StringSplitOptions.RemoveEmptyEntries);
                    if (SameSign(int.Parse(cp[0]), int.Parse(cp[6])) && SameSign(int.Parse(cp[1]), int.Parse(cp[7])) &&
                        SameSign(int.Parse(cp[2]), int.Parse(cp[8])))
                    {
                        int a = 0;
                        for (int i = 6; i < 9; i++)
                        {
                            a += Math.Abs(int.Parse(cp[i]));
                        }

                        particles.Add(index, a);
                    }
                    remains.Add(new Particle(cp, index));
                    index++;
                }
            }

            for(int i = 0; i < 50; i++)
            {
                remains = RemoveCollisions(remains).ToList();
                remains.ForEach( p => p.Move());
            }

            Console.WriteLine("Part one: " + particles.Keys.First(k => particles[k] == particles.Values.Min()));
            Console.WriteLine("Part two: " + remains.Count);
        }

        private static IEnumerable<Particle> RemoveCollisions(List<Particle> particles)
        {
            while (particles.Any())
            {
                var particle = particles.First();
                var collisions = particles.Where(p => p.Position == particle.Position).ToList();
                if (collisions.Count == 1)
                {
                    yield return particle;
                }
                collisions.ForEach(c => particles.Remove(c));
            }
        }

        private static bool SameSign(int num1, int num2)
        {
            if (num1 > 0 && num2 < 0)
                return false;
            if (num1 < 0 && num2 > 0)
                return false;
            return true;
        }
    }

    class Particle
    {
        public Point3D Position { get; set;}
        public Point3D Velocity { get; set; }
        public Point3D Acceleration { get; set; }
        public int ParticleNumber { get; set; }

        public Particle(string[] input, int particleNumber)
        {
            ParticleNumber = particleNumber;
            Position = new Point3D(long.Parse(input[0]), long.Parse(input[1]), long.Parse(input[2]));
            Velocity = new Point3D(long.Parse(input[3]), long.Parse(input[4]), long.Parse(input[5]));
            Acceleration = new Point3D(long.Parse(input[6]), long.Parse(input[7]), long.Parse(input[8]));
        }

        public void Move()
        {
            Velocity.X += Acceleration.X;
            Velocity.Y += Acceleration.Y;
            Velocity.Z += Acceleration.Z;
            Position.X += Velocity.X;
            Position.Y += Velocity.Y;
            Position.Z += Velocity.Z;
        }
    }

    class Point3D
    {
        public long X { get; set; }
        public long Y { get; set; }
        public long Z { get; set; }

        public Point3D(long x, long y, long z)
        {
            X = x;
            Y = y;
            Z = z;
        }

        public static bool operator ==(Point3D point1, Point3D point2)
        {
            return point1.X == point2.X && point1.Y == point2.Y && point1.Z == point2.Z;
        }

        public static bool operator !=(Point3D a, Point3D b)
        {
            return a.X != b.X || a.Y != b.Y || a.Z != b.Z;
        }
    }
}
