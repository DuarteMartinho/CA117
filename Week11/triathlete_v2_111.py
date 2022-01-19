class Triathlete(object):

    def __init__(self, name="", tid=0):
        self.name = name
        self.tid = tid
        self.disciplines = {}

    def __str__(self):
        total = 0
        for k in self.disciplines:
            total += self.disciplines[k]
        return (f'Name: {self.name}\nID: {self.tid}\nRace time: {total}')

    def add_time(self, disciplines, time):
        self.disciplines[disciplines] = time

    def get_time(self, disciplines):
        return self.disciplines[disciplines]
