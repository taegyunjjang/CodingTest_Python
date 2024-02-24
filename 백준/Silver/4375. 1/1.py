import sys

input = sys.stdin.readline

def solution():
    for n in sys.stdin:
        n = int(n)
        degree = 1
        one_number = 1

        while True:
            if one_number % n == 0:
                break

            one_number += 10**degree
            degree += 1

        print(degree)
        
solution()