class DynamicArray:
    
    def __init__(self, capacity: int):
        self.a = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.a[i]

    def set(self, i: int, n: int) -> None:
        self.a[i] = n

    def pushback(self, n: int) -> None:
        self.a.append(n)
        if len(self.a) > self.capacity:
            self.resize()

    def popback(self) -> int:
        return self.a.pop()

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.a)
    
    def getCapacity(self) -> int:
        return self.capacity