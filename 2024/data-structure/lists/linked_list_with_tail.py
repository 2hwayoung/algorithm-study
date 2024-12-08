from node import Node

class LinkedListWithTail(object):
    def __init__(self):
        self.head_ = None
        self.tail_ = None
        self.size_ = 0

    def set_head(self, head_node: Node):
        self.head_ = head_node

    def set_tail(self, tail_node: Node):
        self.tail_ = tail_node

    def size(self):
        return self.size_
    
    def empty(self):
        return self.head_ == None
    
    def value_at(self, index):
        if index < 0 or index >= self.size_:
            raise IndexError('Index out of range')
        current = self.head_
        for _ in range(index):
            current = current.get_next()
        return current.get_data()
    
    def push_front(self, value):
        new_node = Node(value, self.head_)
        self.set_head(new_node)
        if self.tail_ is None:
            self.set_tail(new_node)
        self.size_ += 1

    def pop_front(self):
        if self.empty():
            raise IndexError('Empty List')
        head_node = self.head_
        self.set_head(head_node.get_next())
        if self.head_ is None:
            self.set_tail(None)
        self.size_ -= 1
        return head_node.get_data()
    
    def push_back(self, value):
        new_node = Node(value)
        if self.tail_:
            self.tail_.set_next(new_node)
            self.set_tail(new_node)
        else:
            self.set_head(new_node)
            self.set_tail(new_node)
        self.size_ += 1

    def pop_back(self):
        if self.empty():
            raise IndexError('Empty List')
        # 노드가 하나인 경우
        if self.head_ == self.tail_:
            val = self.head_.get_data()
            self.set_head(None)
            self.set_tail(None)
            self.size_ -= 1
            return val
        
        # tail 직전 노드를 찾아야 함
        current = self.head_
        while current.get_next() != self.tail_:
            current = current.get_next()

        val = self.tail_.get_data()
        current.set_next(None)
        self.set_tail(current)
        self.size_ -= 1
        return val
    
    def front(self):
        if self.empty():
            raise IndexError('Empty List')
        return self.head_.get_data()
    
    def back(self):
        if self.empty():
            raise IndexError('Empty List')
        return self.tail_.get_data()
    
    def insert(self, index, value):
        if index < 0 or index > self.size_:
            raise IndexError('Index out of range')

        if index == 0:
            self.push_front(value)
        elif index == self.size_:
            self.push_back(value)
        else:
            prev = self.head_
            for _ in range(index - 1):
                prev = prev.get_next()
            next_node = prev.get_next()
            new_node = Node(value, next_node)
            prev.set_next(new_node)
            if next_node is None:
                self.set_tail(new_node)
            self.size_ += 1
    
    def erase(self, index):
        if index < 0 or index >= self.size_:
            raise IndexError('Index out of range')

        if index == 0:
            return self.pop_front()
        else:
            prev = self.head_
            for _ in range(index - 1):
                prev = prev.get_next()
            node_to_remove = prev.get_next()
            next_node = node_to_remove.get_next()
            prev.set_next(next_node)
            if next_node is None:
                self.set_tail(prev)
            self.size_ -= 1
            return node_to_remove.get_data()

    def value_n_from_end(self, n):
        # 뒤에서 n번째 (n=0이면 마지막 원소)
        if n < 0 or n >= self.size_:
            raise IndexError('Index out of range')
        target_index = self.size_ - 1 - n
        return self.value_at(target_index)
    
    def reverse(self):
        prev = None
        current = self.head_
        self.set_tail(self.head_)
        while current:
            next_node = current.get_next()
            current.set_next(prev)
            prev = current
            current = next_node
        self.set_head(prev)
    
    def remove_value(self, value):
        if self.empty():
            return False

        current = self.head_
        prev = None
        while current:
            if current.get_data() == value:
                if prev is None:
                    # 제거 대상이 head일 경우
                    self.set_head(current.get_next())
                    if self.head_ is None:
                        self.set_tail(None)
                else:
                    prev.set_next(current.get_next())
                    if current.get_next() is None:
                        self.set_tail(prev)
                self.size_ -= 1
                return True
            prev = current
            current = current.get_next()

if __name__ == "__main__":
    ll = LinkedListWithTail()

    # Test push_front and push_back
    ll.push_front(10)
    ll.push_back(20)
    ll.push_front(5)
    print("After push_front and push_back:", [ll.value_at(i) for i in range(ll.size())])

    # Test pop_front and pop_back
    print("Pop front:", ll.pop_front())  # 5
    print("Pop back:", ll.pop_back())   # 20
    print("After pop operations:", [ll.value_at(i) for i in range(ll.size())])

    # Test size and empty
    print("Size:", ll.size())           # 1
    print("Is empty:", ll.empty())      # False

    # Test insert and erase
    ll.push_back(30)
    ll.insert(1, 25)
    print("After insert:", [ll.value_at(i) for i in range(ll.size())])
    ll.erase(1)
    print("After erase:", [ll.value_at(i) for i in range(ll.size())])

    # Test value_n_from_end
    ll.push_back(40)
    ll.push_back(50)
    print("Value 2nd from end:", ll.value_n_from_end(2))  # 10

    # Test reverse
    ll.reverse()
    print("After reverse:", [ll.value_at(i) for i in range(ll.size())])

    # Test remove_value
    ll.remove_value(40)
    print("After remove_value:", [ll.value_at(i) for i in range(ll.size())])