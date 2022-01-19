import math

binops = {
    "+": "add",
    "-": "minus",
    "*": "multi",
    "/": "div",
}

class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

def add(val1, val2):
    # print(f'Adding {val1} + {val2}')
    return val1 + val2

def minus(val1, val2):
    # print(f'Subtracting {val1} - {val2}')
    return val1 - val2

def multi(val1, val2):
    # print(f'Multiplying {val1} * {val2}')
    return val1 * val2

def div(val1, val2):
    # print(f'Dividing {val1} / {val2}')
    return val1 / val2

def calculator(line):
    line = line.split()
    s = Stack()
    total = 0
    # print("-------------------------------")
    # print(line)
    for c in line:
        try:
            float(c)
            isDIGIT = True
        except ValueError:
            isDIGIT = False
        if isDIGIT:
            s.push(float(c))
        elif c == 'n':
            if not s.is_empty():
                val = s.pop()
                val = val * -1
                s.push(val)
            else:
                total = total * -1
        elif c == 'r':
            if total == 0:
                total = s.pop()
            # print(total)
            total = math.sqrt(total)
        else:
            try:
                if total == 0:
                    val2 = s.pop()
                    val1 = s.pop()
                else:
                    val2 = total
                    val1 = s.pop()
                if binops[c] == "add":
                    ans = add(val1, val2)
                elif binops[c] == "minus":
                    ans = minus(val1, val2)
                elif binops[c] == "multi":
                    ans = multi(val1, val2)
                elif binops[c] == "div":
                    ans = div(val1, val2)
                total = ans
            except KeyError:
                return
        # print(total, c)
    if total == 0 and len(s) == 1:
        total = s.top()
    # print(line, s.top(), s.pop())
    return total
