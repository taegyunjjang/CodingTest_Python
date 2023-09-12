def solution(n, left, right):
    result = []

    for row in range(left // n, (right // n) + 1):
        # row * n : 현재 행에서의 열의 합. 특정 행에서의 열 인덱스 계산
        start = max(left - row * n, 0)
        end = min(right - row * n, n - 1)
        for col in range(start, end + 1):
            result.append(max(row, col) + 1)

    return result

# 1 2 3 4           # 1 2 3 4 | 2 2 3 4 | 3 3 3 4 | 4 4 4 4
# 2 2 3 4
# 3 3 3 4
# 4 4 4 4