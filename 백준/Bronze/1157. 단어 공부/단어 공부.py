import sys

input = sys.stdin.readline
S = input().rstrip().upper()
dic = {chr(i):0 for i in range(65, 91)}

for ch in S:
    dic[ch] += 1

l = sorted(dic.items(), key=lambda x: -x[1])

if l[0][1] == l[1][1]:
    print('?')
else:
    print(l[0][0])