from collections import deque

def solution(numbers):
    num_len = len(numbers)
    answer = [-1] * num_len
    
    stack = deque()
    stack.append(0)
    
    for i in range(1, num_len):
        pivot_num = numbers[i]
        while stack:
            if numbers[stack[-1]] < pivot_num:
                answer[stack.pop()] = pivot_num
            else:
                break   
        stack.append(i)
        
    return answer