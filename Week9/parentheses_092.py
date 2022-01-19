d = {
    "}": "{",
    "]": "[",
    ")": "("
}

class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        try:
            return self.l.pop()
        except IndexError:
            return "nil"

    def top(self):
        try:
            return self.l[-1]
        except IndexError:
            return "nil"

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

def matcher(line):
    s = Stack()
    for c in line:
        if c in d.values():
            s.push(c)

        if c in d.keys():
            if d[c] != s.pop():
                return False
    return s.is_empty()
