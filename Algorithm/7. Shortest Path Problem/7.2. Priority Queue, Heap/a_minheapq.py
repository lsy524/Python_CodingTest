import heapq

# 오름차순 힙 정렵 = Min Heap 
# 파이썬에서 heapq은 기본적으로 오름차순 정렬 
def minheapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입  
    for i in iterable:
        heapq.heappush(h, i)
    
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 result리스트에 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result 

result = minheapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

print(result)