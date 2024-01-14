def solution(numbers, target):
    queue = [0]
    for num in numbers:
        tmp = []
        queue_size = len(queue)
        
        for _ in range(queue_size):
            # dequeue
            front_q = queue.pop()
            
            # BFS
            tmp.append(num + front_q)
            tmp.append(-num + front_q)
            
        # enqueue
        queue = tmp
        
    return queue.count(target)