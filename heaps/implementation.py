class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        curr = len(self.heap) - 1
        # Only start swapping if curr > parent
        while curr > 0 and self.heap[curr] > self.heap[self._parent(curr)]:
            self._swap(curr, self._parent(curr))
            curr = self._parent(curr)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return


my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(70)
my_heap.insert(60)
my_heap.insert(55)
my_heap.insert(50)
my_heap.insert(80)
print(my_heap.heap)

my_heap.remove()
print(my_heap.heap)
