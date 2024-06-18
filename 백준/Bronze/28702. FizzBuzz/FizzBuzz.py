import sys
input = sys.stdin.readline


def solution():
    A = [input().rstrip() for _ in range(3)]
    for i in range(3):
        if A[i].isdigit():
            tmp = int(A[i]) + (3 - i)
            break
    
    if tmp % 3 == 0 and tmp % 5 == 0:
        print("FizzBuzz")
    elif tmp % 3 == 0:
        print("Fizz")
    elif tmp % 5 == 0:
        print("Buzz")
    else:
        print(tmp)
                        
solution()