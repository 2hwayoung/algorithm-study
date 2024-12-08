
class QueueWithFixedSize:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0 
        self.rear = 0
        self.size = 0
    
    def enqueue(self, value):
        if self.full():
            raise OverflowError("Queue is full")
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.empty():
            raise IndexError("Queue is empty")
        node = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return node

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.capacity

    def __str__(self):
        return f"Queue: {self.queue}, Front: {self.front}, Rear: {self.rear}, Size: {self.size}"