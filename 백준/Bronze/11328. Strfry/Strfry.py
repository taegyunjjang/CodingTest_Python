import sys
input = sys.stdin.readline

answer = []

N = int(input())
for _ in range(N):
    str1, str2 = input().rstrip().split()
    if sorted(str1) == sorted(str2):
        answer.append("Possible")
    else:
        answer.append("Impossible")

for ch in answer:
    print(ch)