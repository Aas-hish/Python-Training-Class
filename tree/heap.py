import heapq

elements = [20, 30, 3, 45, 6, 78, 9, 2]
min_heap = []
max_heap=[]

for i in elements:
    heapq.heappush(min_heap, i)

print("Heap:", min_heap)

sorted_heap = []
while min_heap:
    sorted_heap.append(heapq.heappop(min_heap))

print("Sorted:", sorted_heap)



for i in elements:
    heapq.heappush(max_heap,-i)
print("Max-Heap",max_heap)

sorted_max_heap = []
while max_heap:
    sorted_max_heap.append(-heapq.heappop(max_heap))
print("Sorted Max Heap",sorted_max_heap)


