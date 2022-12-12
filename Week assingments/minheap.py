from sys import maxsize


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1
    
    def swap(self, i, x):
        self.heap[i], self.heap[x] = self.heap[x], self.heap[i]

    def push(self, key):
        self.size += 1
        self.heap[self.size] = key
        print(self.parent(self.size))
        print("lisätään: " + str(key) + " parent: " + str(self.heap[self.parent(self.size)]))
            

    def pop(self):
        return self.heap[0]
    
    def print(self):
        lenght = len(self.heap)
        print(self.heap)


if __name__ == "__main__":
    items = [4, 8, 6, 5, 1, 2, 3]
    heap = MinHeap()
    [heap.push(key) for key in items]
    heap.print()        # 1 4 2 8 5 6 3 
    print(heap.pop())   # 1
    heap.print()        # 2 4 3 8 5 6 