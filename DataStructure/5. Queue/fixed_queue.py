# 고정 길이 큐 클래스 FixedQueue 구현 

class FixedQueue :
    
    # 비어 있는 FixedQueue에서 dequeue 또는 peek할 때 내보내는 예외 처리 
    class Empty(Exception):
        pass

    # 가득 차 있는 FixedQueue에서 enqueue할 때 내보내는 예외 처리
    class Full(Exception):
        pass
    
    # 큐 초기화 
    def __init__(self, capacity):
        self.no = 0                    # 현재 데이터 개수 
        self.front = 0                 # 맨 앞 원소 커서(인덱스)
        self.rear = 0                  # 맨 끝 원소 커서(인덱스)
        self.capacity = capacity       # 큐의 크기 
        self.que = [None] * capacity   # 큐의 본체
    
    # 큐에 있는 모든 데이터 개수를 반환 
    def __len__(self):
        return self.no
    
    # 큐가 비어 있는지 판단 
    def is_empty(self):
        return self.no <= 0
    
    #큐가 가득 차 있는지 판단
    def is_full(self):
        return self.no >= self.capacity

    # 데이터 x를 인큐 
    def enqueue(self, value):
        if self.is_full() :
            raise FixedQueue.Full       # 큐가 가득 차 있는 경우 예외 처리 발생
        
        self.que[self.rear] = value
        self.no += 1
        self.rear += 1

        if self.rear == self.capacity:
            self.rear = 0

    # 데이터를 디큐 
    def dequeue(self):
        if self.is_empty():
            raise FixedQueue.Empty      # 큐가 비어있는 경우 예외 처리 발생 
        x = self.que[self.front]
        self.no -= 1
        self.front +=1
        if self.front == self.capacity :
            self.front = 0 

        return x
    
    # 큐에서 데이터를 peek(맨 앞 데이터를 들여다봄)
    def peek(self):        
        if self.is_empty():
            raise FixedQueue.Empty      # 큐가 비어 있는 경우 예외 처리 발생

        return self.que[self.front]
    
    # 큐에서 value를 찾아 인덱스를 반환(없으면 -1 반환)
    def find(self, value):
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value : # 검색 성공
                return idx               
        return -1                       # 검색 실패

    # 큐에 있는 value의 개수 반환
    def count(self, value):
        cnt = 0

        for i in range(self.no):        # 큐 데이터를 선형 검색
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:  # 검색 성공
                cnt += 1
        return cnt                      # 검색 실패

    # 큐에 value가 있는지 판단
    def __contains__(self, value):
        return self.count(value)

    # 큐의 모든 데이터를 비움 
    def clear(self):
        self.no = self.front = self.rear = 0

    # 모든 데이터를 맨 앞부터 맨 끝 순으로 출력
    def dump(self):
        if self.is_empty():             # 큐가 비어있음
            print("Queue is Empty")
        else :
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=" ")
            print()