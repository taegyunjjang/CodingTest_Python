import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

def duplicate_combinations(elements, k):
    combinations = combinations_with_replacement(elements, k)
    result = []
    for combo in combinations:
        counts = [0] * len(elements)
        for element in combo:
            counts[elements.index(element)] += 1
        result.append(counts)
    return result

def solution():
    answer = set()
    N = int(input())
    H = duplicate_combinations(['I', 'V', 'X', 'L'], N)
    
    for h in H:
        I, V, X, L = h
        answer.add(1*I + 5*V + 10*X + 50*L)

    print(len(answer))

solution()