import sys


input = sys.stdin.readline
name = input().rstrip()
answer = ""

odd_cnt = 0
dic = {chr(i):name.count(chr(i)) for i in range(65, 91)}
for val in dic.values():
    if val % 2 != 0:
        odd_cnt += 1

# 길이가 짝수면 원소의 개수가 모두 짝수여야 팰린드롬
if len(name) % 2 == 0 and odd_cnt == 0:
    for ch, cnt in dic.items():
        if cnt:
            answer += ch * (cnt//2)
    answer += answer[::-1]
# 길이가 홀수면 원소의 개수가 홀수인 원소가 유일해야 팰린드롬
elif len(name) % 2 != 0 and odd_cnt == 1:
    center = ''
    for ch, cnt in dic.items():
        if cnt == 1: 
            center = ch
        elif cnt % 2 == 0:
            answer += ch * (cnt//2)
        else:
            answer += ch * (cnt//2)
            center = ch
    answer += center + answer[::-1]
else:
    answer = "I'm Sorry Hansoo"

print(answer)
