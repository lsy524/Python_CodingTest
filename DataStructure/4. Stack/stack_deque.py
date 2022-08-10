# 고정 길이 스택 클래스를 deque를 사용해서 구현 

from collections import deque

# 고정 길이 스택 클래스 
class StackDeque:

    # 스택 초기화 
    def __init__(self, maxlen = 265) :
        self.__stk = deque([], maxlen)
        self.capacity = maxlen

    # 스택에 쌓여 잇는 데이터 개수를 반환
    def __len__(self):
        return len(self.__stk)

    # 스택이 비어 있는지 판단
    def is_empty(self):
        return not self.__stk 
    
    # 스택이 가득차 있는지 판단
    def is_full(self):
        return len(self.__stk) == self.__stk.maxlen
    
    # 스택에 value를 push 
    def push(self, value):
        self.__stk.append(value)
    
    # 스택에 데이터를 pop
    def pop(self):
        return self.__stk.pop()

    # 스택에 데이터를 peek
    def peek(self):
        return self.__stk[-1]

    # 스택을 비움 
    def clear(self):
        return self.__stk.clear()
    
    # 스택에서 value를 찾아 인덱스를 반환(찾지 못하면 -1 반환)
    def find(self, value):
        try :
            return self.__stk.index(value)
        except ValueError:
            return -1 
    
    # 스택에 포함되어 있는 value의 개수를 반환
    def count(self, value):
        return self.__stk.count(value)

    # 스택에 value가 포함되어 있는 지 판단 
    def __contains__(self, value):
        return self.count(value)
    
    # 스택 안에 있는 모든 데이터를 나열(바닥 -> 꼭대기)
    def dump(self):
        print(list(self.__stk))
    