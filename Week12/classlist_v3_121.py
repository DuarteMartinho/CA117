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

class Classlist(object):

    def __init__(self):
        self.students = {}
        self.courses = {}

    def __str__(self):
        sorted_dict = {}
        for k in sorted(self.students):
            sorted_dict[k] = self.students[k]
        ans = ""
        for k in sorted_dict:
            ans += f'Name: {sorted_dict[k].name}\nAddress: {sorted_dict[k].address}\nID: {sorted_dict[k].sid}\n'
        return ans.rstrip()

    def add(self, student):
        self.students[student.sid] = student
        for k in student.marks:
            if k in self.courses:
                self.courses[k] += 1
            else:
                self.courses[k] = 1

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

    def least_popular_module(self):
        courses_to_list = sorted(self.courses.keys())
        return courses_to_list[-1]
