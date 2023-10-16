class CircularQueue:
    def __init__(self, max_size):
        self.__items = [None] * max_size
        self.__max_size = max_size
        self.__front = self.__rear = 0

    def isEmpty(self):
        return all(item is None for item in self.__items)

    def isFull(self):
        return ((self.__rear + 1) % self.__max_size) == self.__front

    def enqueue(self, item):
        if self.isFull():
            print('Queue Overflow Error')
            return

        self.__items[self.__rear] = item
        self.__rear = (self.__rear + 1) % self.__max_size

    def dequeue(self):
        if self.isEmpty():
            print('Queue Underflow Error')
            return

        self.__items[self.__front] = None
        self.__front = (self.__front + 1) % self.__max_size

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__items[self.__front]

    def contains(self, item):
        return item in self.__items