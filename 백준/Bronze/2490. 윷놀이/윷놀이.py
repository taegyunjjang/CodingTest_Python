dic = {3:'A', 2:'B', 1:'C', 0:'D', 4:'E'}
answer = []

for _ in range(3):
    answer.append(dic[list(map(int, input().split())).count(1)])

for num in answer:
    print(num)