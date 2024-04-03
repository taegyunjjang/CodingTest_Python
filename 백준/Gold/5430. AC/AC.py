from collections import deque
import sys
input = sys.stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        is_stop = False
        command = input().rstrip()
        
        N = int(input())
        arr = input().rstrip()[1:-1]
                
        dq = deque(arr.split(','))
            
        if N == 0 and command.count('D'):
            print("error")
        else:
            is_reverse = False
            for cmd in command:
                if cmd == 'R':
                    is_reverse = not is_reverse
                else:
                    if len(dq) == 0:
                        print("error")
                        is_stop = True
                        break
                    
                    if is_reverse:
                        dq.pop()
                    else:
                        dq.popleft()  
                        
            if is_stop:
                continue
            
            if command.count('R') % 2 != 0:
                dq.reverse()
            
            result = ','.join(dq)   
            print('[' + result + ']')      

solution()