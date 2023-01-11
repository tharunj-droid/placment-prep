from collections import deque

class Queue:
    def __init__(self):
        self.buffer=deque()

    def enqueue(self,value):
        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)


q=Queue()
q.enqueue(100)
q.enqueue(120)
q.enqueue(130)
print(q)
print(q.size())
print(q.dequeue())
