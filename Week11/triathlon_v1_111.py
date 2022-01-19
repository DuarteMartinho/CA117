class Triathlete(object):

    def __init__(self, name="", tid=0):
        self.name = name
        self.tid = tid

    def __str__(self):
        return (f'Name: {self.name}\nID: {self.tid}')

class Triathlon(object):

    def __init__(self):
        self.people = {}

    def lookup(self, tid):
        for k in self.people:
            if k == tid:
                return self.people[k]
        return None

    def add(self, other):
        self.people[other.tid] = other

    def remove(self, other):
        remove = False
        for k in self.people:
            if k == other:
                remove = True
        if remove:
            self.people.pop(other)

    def __eq__(self, other):
        return self == other
