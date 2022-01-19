class Student(object):

    def __init__(self, name="", address="", sid=0):
        self.name = name
        self.address = address
        self.sid = sid

    def __eq__(self, other):
        return self == other

    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nID: {self.sid}'

class Classlist(object):

    def __init__(self):
        self.students = {}

    def add(self, student):
        self.students[student.sid] = student

    def lookup(self, sid):
        try:
            return self.students[sid]
        except KeyError:
            return None

    def remove(self, sid):
        remove = False
        for k in self.students:
            if k == sid:
                remove = True
        if remove:
            self.students.pop(sid)
