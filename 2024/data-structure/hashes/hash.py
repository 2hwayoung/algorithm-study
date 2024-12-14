
class HashTable:
    def __init__(self, size = 10):
        self.size = size
        self.table = [None] * self.size  # Initialize the hash table with `None`

    def hash(self, key):
        """
        Hash function to map a key to an index in the hash table.
        Assumes the key is an integer.
        """
        return key % self.size

    def add(self, key, value):
        """
        Add a key-value pair to the hash table.
        If the key already exists, update the value.
        """
        index = self.hash(key)
        original_index = index  # Save the original index to detect cycles

        while self.table[index] is not None:
            if self.table[index][0] == key:
                # Key already exists, update the value
                self.table[index][1] = value
                return
            index = (index + 1) % self.size  # Linear probing
            if original_index == index:  # Table is full
                raise Exception("HashTable is full")
    
        # Insert the new key-value pair
        self.table[index] = (key, value)

    def exists(self, key):
        """
        Check if a key exists in the hash table.
        """
        index = self.hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return True
            index = (index + 1) % self.size
            if index == original_index:  # Full cycle completed
                break
        return False
    
    
    def get(self, key):
        """
        Get the value associated with a key.
        """
        index = self.hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        raise KeyError("Key not found")
    
    def remove(self, key):
        """
        Remove a key-value pair from the hash table.
        """
        index = self.hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                # Rehash all subsequent elements until we find an empty slot
                next_index = (index + 1) % self.size
                while self.table[next_index] is not None:
                    rehash_key, rehash_value = self.table[next_index]
                    self.table[next_index] = None
                    self.add(rehash_key, rehash_value)
                    next_index = (next_index + 1) % self.size
                return
            index = (index + 1) % self.size
            if index == original_index:
                break
        raise KeyError("Key not found")

    def __str__(self):
        return str([item for item in self.table])
    
hash_table = HashTable(5)
hash_table.add(1, "One")
hash_table.add(6, "Six")  # Collision, linear probing will resolve it
hash_table.add(11, "Eleven")  # Collision again
print(hash_table.exists(6))  # True
print(hash_table.get(11))  # "Eleven"
hash_table.remove(6)
print(hash_table.exists(6))  # False
print(hash_table)