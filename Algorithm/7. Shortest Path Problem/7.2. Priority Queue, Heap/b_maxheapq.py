import heapq 

# 내림차순 힙 정렬 = Max Heap
def maxheapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for i in iterable:
        heapq.heappush(h, -i) # 힙에 삽입하기 전에 데이터의 부호를 바꿈
        
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 result리스트에 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h)) # 힙에서 데이터를 꺼낼 때 부호를 바꿈
    return result 

result = maxheapsort([1,3,5,7,9,2,4,6,8,0])

print(result)