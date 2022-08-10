# stack으로 재귀함수 구현 

class Stacked:
    class Empty(Exception): 
        pass 

    class Full(Exception):
        pass

    def __init__(self, capacity=256) :
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
        
    def __len__(self):
        return self.ptr

    def is_empty(self):
        return self.ptr <= 0 
    
    def is_full(self):
        return self.ptr >= self.capacity

    def push(self, value):
        if self.is_full() :
            raise Stacked.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.is_empty():
            raise Stacked.Empty
        
        self.ptr -= 1

        return self.stk[self.ptr]

def recurStack(n):
    s = Stacked(n)

    while True :
        if n > 0:
            s.push(n)
            n -= 1 
            continue 

        if not s.is_empty() :
            n = s.pop()
            print(n)
            n -= 2
            continue
        break
            
x = int(input())
recurStack(x)