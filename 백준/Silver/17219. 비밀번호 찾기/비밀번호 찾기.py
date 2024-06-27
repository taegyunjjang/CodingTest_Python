import sys
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    dic = {}
    for _ in range(N):
        site, pw = input().split()
        dic[site] = pw
    
    for _ in range(M):
        search_site = input().rstrip()
        print(dic[search_site])


solution()