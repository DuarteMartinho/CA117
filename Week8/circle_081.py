#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other):
        x, y = other.x - self.x, other.y - self.y
        return Point(x, y)

class Circle(object):

    def __init__(self, centre, radius=0):
        self.centre = centre.x, centre.y
        self.radius = radius

    def __str__(self):
        return "Centre: {}\nRadius: {}".format(self.centre, self.radius)

    def __add__(self, other):
        x, y = (self.centre[0] + other.centre[0], self.centre[1] + other.centre[1])
        x, y = (x / 2, y / 2)
        centre = Point(x, y)
        radius = self.radius + other.radius
        return Circle(centre, radius)
