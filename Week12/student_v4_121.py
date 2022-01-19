class Student(object):

    def __init__(self, name="", address="", sid=0):
        self.name = name
        self.address = address
        self.sid = sid
        self.marks = {}
        self.totalExams = 0
        self.totalMarks = 0
        self.average = 0

    def __eq__(self, other):
        return self.average == other.average

    def __lt__(self, other):
        return self.average < other.average

    def __gt__(self, other):
        return self.average > other.average

    def __str__(self):
        if self.totalExams != 0:
           self.average = self.totalMarks / self.totalExams
        return f'Name: {self.name}\nAddress: {self.address}\nID: {self.sid}\nAverage mark: {self.average:.2f}'

    def add_mark(self, code, mark):
        self.marks[code] = mark
        self.totalMarks += mark
        self.totalExams += 1

    def get_mark(self, code):
        try:
            return self.marks[code]
        except KeyError:
            return f'Not registered for module'
