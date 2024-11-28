from node import Node

class LinkedList(object):
    def __init__(self):
        self.head_ = None

    def set_head(self, head_node: Node):
        self.head_ = head_node

    def __len__(self):
        count = 0
        current = self.head_
        while current:
            count += 1
            current = current.get_next()
        return count


    def __str__(self):
        current = self.head_
        output = ""
        while current:
            output += str(current) + " -> "
            current = current.get_next()
        return output

    # Pops an item from the front of the list
    def pop(self):
        if self.head_:
            self.set_head(self.head_.get_next())
        else:
            raise IndexError("Unable to pop from empty list")

    # Returns true if list contains the given value.
    def contains(self, value):
        current = self.head_
        while current:
            if value == current.get_data():
                return True
            current = current.get_next()
        return False
    
    # Deletes all instances of given value in list.
    def delete(self, value):
        current = self.head_
        prev = None
        while current:
            if current.get_data() == value:
                if prev:
                    prev.set_next(current.get_next())
                else:
                    self.set_head(current.get_next())
            else:
                prev = current
            current = current.get_next()

    # Pushes an item on the front of the list.
    def push(self, value):
        node = Node(value)
        node.set_next(self.head_)
        self.set_head(node)
            

    def append(self, value):
        node = Node(value)
        current = self.head_
        if not current:
            self.set_head(node)
            return
        
        while current.get_next():
            current = current.get_next()
        current.set_next(node)

    def reverse(self):
        prev = None
        current = self.head_
        while current:
            next_node = current.get_next()
            current.set_next(prev)
            prev = current
            current = next_node
        self.set_head(prev)