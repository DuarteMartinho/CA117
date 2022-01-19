class Triathlete(object):

    def __init__(self, name="", tid=0):
        self.name = name
        self.tid = tid
        self.disciplines = {}
        self.total = 0

    def __str__(self):
        return (f'Name: {self.name}\nID: {self.tid}\nRace time: {self.total}')

    def add_time(self, disciplines, time):
        self.disciplines[disciplines] = time
        self.total += time

    def get_time(self, disciplines):
        return self.disciplines[disciplines]

    def __eq__(self, other):
        return self.total == other.total

    def __lt__(self, other):
        return self.total < other.total

    def __gt__(self, other):
        return self.total > other.total
