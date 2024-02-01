import sys
input = sys.stdin.readline

answer = 0
alp_dic1 = {chr(i + 97):0 for i in range(26)}
alp_dic2 = {chr(i + 97):0 for i in range(26)}

str1 = input().rstrip()
str2 = input().rstrip()

for ch in str1:
    alp_dic1[ch] += 1

for ch in str2:
    alp_dic2[ch] += 1

for val1, val2 in zip(alp_dic1.values(), alp_dic2.values()):
    answer += abs(val1 - val2)

print(answer)