from stream_wrapper import StreamWrapper

class Vec2:
    """2 dimensional vector."""

    __slots__ = ("x","y",)

    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        """`x` coordinate of the vector"""
        self.y = y
        """`y` coordinate of the vector"""

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x
        y = self.y
        if isinstance(other, Vec2):
            x = self.x + other.x
            y = self.y + other.y
        elif isinstance(other, float):
            x = self.x + other
            y = self.y + other
        return Vec2(x, y)

    def __sub__(self, other):
        x = self.x
        y = self.y
        if isinstance(other, Vec2):
            x = self.x - other.x
            y = self.y - other.y
        elif isinstance(other, (float, int)):
            x = self.x - other
            y = self.y - other
        return Vec2(x, y)

    def __mul__(self, other):
        x = self.x
        y = self.y
        if isinstance(other, Vec2):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (float, int)):
            x = self.x * other
            y = self.y * other
        return Vec2(x, y)

    def __truediv__(self, other):
        x = self.x
        y = self.y
        if isinstance(other, Vec2):
            return self.x / other.x + self.y / other.y
        elif isinstance(other, (float, int)):
            x = self.x / other
            y = self.y / other
        return Vec2(x, y)


    @staticmethod
    def read_from(stream: StreamWrapper) -> "Vec2":
        """Read Vec2 from input stream
        """
        x = stream.read_double()
        y = stream.read_double()
        return Vec2(x, y)
    
    def write_to(self, stream: StreamWrapper):
        """Write Vec2 to output stream
        """
        stream.write_double(self.x)
        stream.write_double(self.y)
    
    def __repr__(self):
        return "Vec2(" + \
            repr(self.x) + \
            ", " + \
            repr(self.y) + \
            ")"