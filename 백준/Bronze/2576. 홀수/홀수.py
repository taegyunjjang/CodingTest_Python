answer = []

for _ in range(7):
    num = int(input())
    if num % 2 != 0:
        answer.append(num)

if answer:
    print(sum(answer))
    print(min(answer))
else:
    print("-1")