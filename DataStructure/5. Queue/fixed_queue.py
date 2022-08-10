class FixedQueue :
    
    class Empty(Exception):
        pass

    class Full(Exception):
        pass
    
    def __init__(self, capacity):
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity
    
    def __len__(self):
        return self.no
    
    def is_empty(self):
        return self.no <= 0
    
    def is_full(self):
        return self.no >= self.capacity

    def enqueue(self, value):
        if self.is_full() :
            raise FixedQueue.Full
        
        self.que[self.rear] = value
        self.no += 1
        self.rear += 1

        if self.rear == self.capacity:
            self.rear = 0

    def dequeue(self):
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.no -= 1
        self.front +=1
        if self.front == self.capacity :
            self.front = 0 

        return x
    
    def peek(self):        
        if self.is_empty():
            raise FixedQueue.Empty

        return self.que[self.front]
    
    def find(self, value):
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value :
                return idx 
        return -1 

    def count(self, value):
        cnt = 0

        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                cnt += 1
        return cnt 

    
    def __contains__(self, value):
        return self.count(value)


    def clear(self):
        self.no = self.front = self.rear = 0

    def dump(self):
        if self.is_empty():
            print("Queue is Empty")
        else :
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=" ")
            print()