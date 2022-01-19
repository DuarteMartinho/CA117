class Student(object):

    def __init__(self, name="", address="", sid=0):
        self.name = name
        self.address = address
        self.sid = sid

    def __eq__(self, other):
        return self == other

    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nID: {self.sid}'
