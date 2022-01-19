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

class Triathlon(object):
    def __init__(self):
        self.people = {}

    def __str__(self):
        sorted_dict = {}
        for k, v in sorted(self.people.items()):
            sorted_dict[v.name] = v.tid
        ans = ""
        for k in sorted(sorted_dict):
            ans += f'Name: {k}\nID: {sorted_dict[k]}\n'
        return ans.rstrip()

    def lookup(self, tid):
        for k in self.people:
            if k == tid:
                return self.people[k]
        return None

    def add(self, other):
        self.people[other.tid] = other

    def best(self):
        shortest_time = 0
        tid = 0
        for k, v in sorted(self.people.items()):
            if shortest_time == 0:
                shortest_time = v.total
                tid = v.tid
            elif shortest_time > v.total:
                shortest_time = v.total
                tid = v.tid
        return self.people[tid]

    def worst(self):
        biggest_time = 0
        tid = 0
        for k, v in sorted(self.people.items()):
            if biggest_time < v.total:
                biggest_time = v.total
                tid = v.tid
        return self.people[tid]

    def remove(self, other):
        remove = False
        for k in self.people:
            if k == other:
                remove = True
        if remove:
            self.people.pop(other)

    def __eq__(self, other):
        return self == other
