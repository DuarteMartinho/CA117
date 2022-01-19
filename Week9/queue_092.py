class Queue(object):

    def __init__(self):
        self.q = []

    def enqueue(self, e):
        self.q.append(e)

    def dequeue(self):
        val = self.q[0]
        self.q.pop(0)
        return val

    def first(self):
        try:
            return self.q[0]
        except IndexError:
            return 'Error'

    def is_empty(self):
        return len(self.q) == 0

    def __len__(self):
        return len(self.q)
