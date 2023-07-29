def solution(n):
    for i in range(15):
        if 1 + 7 * i <= n <= 7 * (i + 1):
            return i + 1

# 1~7 : 1
# 8~14 : 2
# 15~21 :3
# 92~98 : 14
# 99~100 : 15