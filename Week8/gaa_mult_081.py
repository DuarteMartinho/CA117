#!/usr/bin/env python3

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return "{} goal(s) and {} point(s)".format(self.goals, self.points)

    def __eq__(self, opponent):
        return ((self.goals * 3 + self.points) == (opponent.goals * 3 + opponent.points))

    def __nq__(self, opponent):
        return ((self.goals * 3 + self.points) != (opponent.goals * 3 + opponent.points))

    def __gt__(self, opponent):
        return ((self.goals * 3 + self.points) > (opponent.goals * 3 + opponent.points))

    def __lt__(self, opponent):
        return ((self.goals * 3 + self.points) < (opponent.goals * 3 + opponent.points))

    def __ge__(self, opponent):
        return ((self.goals * 3 + self.points) >= (opponent.goals * 3 + opponent.points))

    def __le__(self, opponent):
        return ((self.goals * 3 + self.points) <= (opponent.goals * 3 + opponent.points))

    def __add__(self, opponent):
        goals, points = self.goals + opponent.goals, self.points + opponent.points
        return Score(goals, points)

    def __sub__(self, opponent):
        goals, points = self.goals - opponent.goals, self.points - opponent.points
        return Score(goals, points)

    def __iadd__(self, opponent):
        z = self + opponent
        self.goals, self.points = z.goals, z.points
        return self

    def __isub__(self, opponent):
        z = self - opponent
        self.goals, self.points = z.goals, z.points
        return self

    def __mul__(self, mul):
        return Score(self.goals * mul, self.points * mul)

    def __imul__(self, mul):
        z = self * mul
        self.goals, self.points = z.goals, z.points
        return self

    def __rmul__(self, mul):
        return Score(self.goals * mul, self.points * mul)
