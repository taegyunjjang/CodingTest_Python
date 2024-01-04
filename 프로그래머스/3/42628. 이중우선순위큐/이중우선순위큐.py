from heapq import heappush, heappop

def solution(operations):
    min_heap = []
    max_heap = []
    
    for op in operations:
        instruction, num = op.split()
        value = int(num)
        
        if instruction == 'I':
            heappush(min_heap, value)
            heappush(max_heap, -value)
        elif instruction == 'D' and value == -1 and min_heap:
            deleted_item = heappop(min_heap)
            max_heap.remove(-deleted_item)
        elif instruction == 'D' and value == 1 and min_heap:
            deleted_item = heappop(max_heap)
            min_heap.remove(-deleted_item)   
            
    if len(min_heap) == 0:
        return [0, 0]
    
    return[-heappop(max_heap), heappop(min_heap)]