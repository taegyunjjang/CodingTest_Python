import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    S = list(map(int, input().split()))
    
    fact = [1]
    for i in range(1, 21):
        fact.append(fact[-1]*i)
    
    num_list = [i for i in range(1, N + 1)]
    answer = []
    tot = 1
    
    # 소문제 번호 1
    if S[0] == 1:
        k = S[1]
        while N:
            for n in range(1, N + 1):
                if k <= n * fact[N - 1]:
                    answer.append(num_list[n - 1])
                    k -= (n - 1) * fact[N - 1]
                    N -= 1
                    num_list.pop(n - 1)
                    break
        print(*answer)   
    
    # 소문제 번호 2
    else:
        seq =S[1:]
        for num in seq:
            i = num_list.index(num)
            tot += i * fact[N - 1]
            N -= 1
            num_list.pop(i)
        print(tot)
    
solution()