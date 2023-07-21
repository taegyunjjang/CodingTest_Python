def solution(arr):
    row = len(arr)
    column = len(arr[0])
    
    if row < column:
        for _ in range(column - row):
            arr.append([0] * column) 
        return arr
    elif row > column:
        for i in range(row):
            for _ in range(row - column):
                arr[i].append(0)
        return arr
    return arr