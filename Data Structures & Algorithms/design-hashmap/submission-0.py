class MyHashMap:

    def __init__(self):
        self.size = 1000001
        self.arr = [-1] * self.size

    def _hash(self, key:int):
        return (key % self.size)

    def put(self, key: int, value: int) -> None:
        self.arr[self._hash(key)] = value

    def get(self, key: int) -> int:
        return self.arr[self._hash(key)]

    def remove(self, key: int) -> None:
        self.arr[self._hash(key)] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)