from ..lists.linked_list_with_tail import LinkedListWithTail

class QueueWithLinkedList:
    def __init__(self):
        self.queue = LinkedListWithTail()
    
    def enqueue(self, value):
        self.queue.push_front(value)

    def dequeue(self):
        return self.queue.pop_front()

    def isEmpty(self):
        return self.queue.empty()