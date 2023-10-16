class Queue:
    def __init__(self, max_size):
        self.__items = [None] * max_size
        self.__max_size = max_size
        self.__front = self.__rear = -1

    def isEmpty(self):
        return self.__front == self.__rear

    def isFull(self):
        return self.__rear == (self.__max_size - 1)

    def enqueue(self, item):
        if self.isFull():
            print('Queue Overflow Error')
            return

        self.__rear += 1
        self.__items[self.__rear] = item

    def dequeue(self):
        if self.isEmpty():
            print('Queue Underflow Error')
            return

        self.__front += 1
        self.__items[self.__front] = None

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__items[self.__front + 1]

    def contains(self, item):
        return item in self.__items