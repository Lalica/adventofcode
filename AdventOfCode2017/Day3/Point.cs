namespace Day3
{
    class Point
    {
        public int x, y;

        public Point(int p1, int p2)
        {
            x = p1;
            y = p2;
        }

        public override int GetHashCode()
        {
            return x.GetHashCode()+y.GetHashCode();
        }
    }
}
