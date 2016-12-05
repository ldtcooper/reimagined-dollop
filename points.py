#!/usr/bin/env python3

import math

class Point:
    """A two-coordinate point on a Cartesian plane of the form (x,y)"""

    def __init__(self, x, y):
        self.x = x
        if isinstance(self.x, int):
            pass
        elif isinstance(self.x, float):
            pass
        else:
            raise TypeError("Points must be integers or floats!")
        self.y = y
        if isinstance(self.y, int):
            pass
        elif isinstance(self.y, float):
            pass
        else:
            raise TypeError("Points must be integers or floats!")


    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def distance(self, other):
        """Calculates the shortest distance between two points"""
        dist = math.sqrt(((other.x - self.x)**2) + ((other.y - self.y)**2))
        return dist

    def midpoint(self,other):
        """Calculates the midpoint between two points"""
        mp = Point((self.x + other.x)/2, (self.y + other.y)/2)
        return mp

    def quadrant(self):
        """Determines which quadrant the point is in

        Note: A point marked as being in quadrant zero is one that lies on one or more axis.
        """
        if self.x > 0 and self.y > 0:
            quad = 1
        elif self.x < 0 and self.y > 0:
            quad = 2
        elif self.x < 0 and self.y < 0:
            quad = 3
        elif self.x > 0 and self.y < 0:
            quad = 4
        else:
            quad = 0
        return quad



