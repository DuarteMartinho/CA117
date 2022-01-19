class Student(object):

    def __init__(self, name="", address="", sid=0):
        self.name = name
        self.address = address
        self.sid = sid
        self.marks = {}

    def __eq__(self, other):
        return self == other

    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nID: {self.sid}'

    def add_mark(self, code, mark):
        self.marks[code] = mark

    def get_mark(self, code):
        try:
            return self.marks[code]
        except KeyError:
            return f'Not registered for module'
