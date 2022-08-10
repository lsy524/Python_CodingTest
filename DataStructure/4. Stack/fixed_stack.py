# 고정 길이 스택 클래스 FixedStack 구현 

# 고정 길이 스택 클래스 
class FixedStack :

    # 비어있는 FixedStack에 pop 또는 peek할 때 내보내는 예외 처리 
    class Empty(Exception): 
        pass

    # 가득 찬 FixedStack에 push할 때 내보내는 예외 처리 
    class Full(Exception) :
        pass 

    # 스택 초기화 
    def __init__(self, capacity = 256) :
        self.stk = [None] * capacity            # 스택 본체 
        self.capacity = capacity                # 스택 크기 
        self.ptr = 0                            # 스택 포인터(현재 데이터 개수)
    
    # 스택 길이 
    def __len__(self):
        return self.ptr                         # 스택에 쌇여 있는 데이터 개수 반환

    
    def is_empty(self) :
        return self.ptr <= 0                    # 스택이 비어있는 지 판단 
    
    def is_full(self):
        return self.ptr >= self.capacity        # 스택이 가득 차 있는지 판단 

    # 스택에 value를 push 
    def push(self, value):
        if self.is_full() :                     # 스택이 가득 차 있는 경우
            raise FixedStack.Full               # 예외 처리 발생 
        self.stk[self.ptr] = value
        self.ptr += 1
    
    # 스택에 데이터 pop(꼭대기 데이터 꺼냄)
    def pop(self):
        if self.is_empty() :                    # 스택이 비어 있는 경우
            raise FixedStack.Empty              # 예외 처리 발생 

        self.ptr -= 1
        return self.stk[self.ptr]

    # 스택에서 데이터 피크(꼭대기 데이터를 들여다봄)
    def peek(self):
        if self.is_empty():                     # 스택이 비어 있는 경우
            raise FixedStack.Empty              # 예외 처리 발생
        
        return self.stk[self.ptr - 1]

    # 스택을 비움(모든 데이터 삭제)
    def clear(self):
        self.ptr = 0

    # 스택에서 value를 찾아 인덱스를 반환(없으면 -1 반환)
    def find(self, value):
        for i in range(self.ptr -1, -1, -1):    # 꼭대기 쪽부터 선형 검색
            if self.stk[i] == value:
                return i                        # 검색 성공
        return -1                               # 검색 실패 
    
    # 스택에 있는 value 개수를 반환
    def count(self, value):
        cnt = 0
        for i in range(self.ptr):               # 바닥 쪽부터 선형 검색
            if self.stk[i] == value:            # 검색 성공
                cnt += 1
        return cnt 

    # 스택에 value가 있는지 판단 (value is stack)
    def __contains__(self, value):
        return self.count(value)

    # dump(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)
    def dump(self):
        if self.is_empty():                     # 스택이 비어 있음
            print("Stack is Empty")
        else :
            print(self.stk[:self.ptr])