class Stack:
    def __init__(self, max_size):
        self.__items = [None] * max_size
        self.__max_size = max_size
        self.__top = -1

    def isEmpty(self):
        return self.__top == -1

    def isFull(self):
        return self.__top == (self.__max_size - 1)

    def push(self, item):
        if self.isFull():
            print('Stack Overflow Error')
            return

        self.__top += 1
        self.__items[self.__top] = item

    def pop(self):
        if self.isEmpty():
            print('Stack Underflow Error')
            return

        self.__items[self.__top] = None
        self.__top -= 1

    def peek(self):
        return self.__items[self.__top]

    def search(self, item):
        for item_index in range(self.__top, -1, -1):
            if self.__items[item_index] == item:
                return item_index

        return -1