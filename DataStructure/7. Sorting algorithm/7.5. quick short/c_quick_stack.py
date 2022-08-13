from collections import deque
from multiprocessing.sharedctypes import Value

class Stack:
    
    def __init__(self, maxlen = 256):
        self.capacitiy = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self):
        return len(self.__stk)

    def is_empty(self):
        return not self.__stk 

    def is_full(self):
        return len(self.__stk) == self.capacitiy

    
    def push(self, value) :
        self.__stk.append(value)

    def pop(self):
        return self.__stk.pop()

    def peek(self):
        return self.__stk[-1]
    
    def clear(self):
        self.__stk.clear()

    def find(self, value):
        try :
            self.__stk.index(value)
        except ValueError :
            return -1 
    
    def count(self, value):
        return self.__stk.count(value)
    
    def __contains__(self, value):
        return self.count(value)
    
    def dump(self):
        print(list(self.__stk))

