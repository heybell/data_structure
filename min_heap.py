class MinHeap:
    def __init__(self):
        self.__heap = []

    def __get_parent(self, index):
        return (index - 1) // 2

    def __get_left_child(self, index):
        child_index = (index * 2) + 1

        if (child_index + 1) <= len(self.__heap):
            return child_index

        return None

    def __get_right_child(self, index):
        child_index = (index * 2) + 2

        if (child_index + 1) <= len(self.__heap):
            return child_index

        return None

    def __heapify_up(self, index):
        parent_index = self.__get_parent(index)

        while index > 0 and self.__heap[index] < self.__heap[parent_index]:
            self.__heap[index], self.__heap[parent_index] = self.__heap[parent_index], self.__heap[index]
            index = parent_index
            parent_index = self.__get_parent(index)

    def __heapify_down(self, index):
        left_child_index = self.__get_left_child(index)
        right_child_index = self.__get_right_child(index)
        smallest = index

        if left_child_index is not None and self.__heap[left_child_index] < self.__heap[smallest]:
            smallest = left_child_index

        if right_child_index is not None and self.__heap[right_child_index] < self.__heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.__heap[index], self.__heap[smallest] = self.__heap[smallest], self.__heap[index]
            self.__heapify_down(smallest)

    def heap_push(self, data):
        self.__heap.append(data)
        self.__heapify_up(len(self.__heap) - 1)

    def heap_pop(self):
        if len(self.__heap) == 0:
            return None
        if len(self.__heap) == 1:
            return self.__heap.pop()

        root = self.__heap[0]
        self.__heap[0] = self.__heap.pop()
        self.__heapify_down(0)

        return root