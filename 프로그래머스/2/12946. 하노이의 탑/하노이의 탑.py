# 상위 n-1개의 원판들을 2로 이동
# 1개의 원판을 3으로 이동
# 기둥 2의 원판들을 3으로 이동
result = []
def solution(n):
    move(n, 1, 2, 3)
    return result
    
def move(n, src, tmp, des):
    if n > 0:
        move(n - 1, src, des, tmp)
        result.append([src, des])
        move(n - 1, tmp, src, des)