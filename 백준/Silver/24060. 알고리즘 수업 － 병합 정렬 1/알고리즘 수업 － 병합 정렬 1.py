import sys
input = sys.stdin.readline

cnt = 0
answer = -1

def merge_sort(A, p, r, K):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q, K)
        merge_sort(A, q + 1, r, K)
        merge(A, p, q, r, K)

def merge(A, p, q, r, K):
    global cnt, answer
    i = p; j = q + 1; t = 0
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    
    while i <= q:
        tmp.append(A[i])
        i += 1
    
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    i = p; t = 0
    while i <= r:
        A[i] = tmp[t]
        cnt += 1
        if cnt == K:
            answer = A[i]
            break
        t += 1; i += 1
    

N, K = map(int, input().split())
A = list(map(int, input().split()))
merge_sort(A, 0, N - 1, K)
print(answer)

