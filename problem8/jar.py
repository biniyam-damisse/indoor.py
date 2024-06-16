class Jar:
    def __init__(self, capacity=12):
        if capacity > 12:
            raise ValueError("Beyond the jar capacity")
        self._capacity = capacity 
        self._size = 0
    def __str__(self):
        return self.size * "🌞" 
    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Beyond the jar capacity")
        if n > self.capacity:
            raise ValueError("Beyond the jar capacity") 
        self._size += n 
    
    def withdraw(self, n):
        if self.capacity < 0:
            raise ValueError("less than the limit")
        if self.size - n < 0:
            raise ValueError("less than the limit")
        self._size -= n
    
    @property 
    def capacity(self):
        return self._capacity 
    @property 
    def size(self): 
        return self._size


