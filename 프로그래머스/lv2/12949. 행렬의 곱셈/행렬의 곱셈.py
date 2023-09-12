def matrixMul(a1, a2):
    tot = 0
    for i in range(len(a1)):
        tot += a1[i] * a2[i]
    return tot

def solution(arr1, arr2):
    row1, row2 = len(arr1), len(arr2)
    col1, col2 = len(arr1[0]), len(arr2[0])
    answer = [[0 for _ in range(col2)] for _ in range(row1)]
    arr3 = [[0 for _ in range(row2)] for _ in range(col2)]
    for i in range(row2):
        for j in range(col2):
            arr3[j][i] = arr2[i][j]
    
    for i in range(row1):
        for j in range(col2):
            answer[i][j] = matrixMul(arr1[i], arr3[j])
    return answer