import sys

def pooling(ary, tmp, n):
    if n == 2:
        ary = ary[0] + ary[1]
        return sorted(ary)[2]
    else:
        tmp.append(pooling([row[:n//2] for row in ary[:n//2]], tmp, n//2))
        tmp.append(pooling([row[n//2:] for row in ary[:n//2]], tmp, n//2))
        tmp.append(pooling([row[:n//2] for row in ary[n//2:]], tmp, n//2))
        tmp.append(pooling([row[n//2:] for row in ary[n//2:]], tmp, n//2))
    
    return sorted(tmp)[2]

input = sys.stdin.readline
N = int(input())
ary = []
tmp = []
for _ in range(N):
    ary.append(list(map(int, input().split())))

print(pooling(ary, tmp, N))
