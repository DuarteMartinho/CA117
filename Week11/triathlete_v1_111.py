class Triathlete(object):

    def __init__(self, name="", tid=0):
        self.name = name
        self.tid = tid

    def __str__(self):
        return (f'Name: {self.name}\nID: {self.tid}')
