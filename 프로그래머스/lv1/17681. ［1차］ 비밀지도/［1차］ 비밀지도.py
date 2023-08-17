def solution(n, arr1, arr2):
    answer = []
    
    for i, num1 in enumerate(arr1):
        if len(bin(num1)[2:]) != n:
            arr1[i] = '0' * (n - len(bin(num1)[2:])) + bin(num1)[2:]
        else:
            arr1[i] = bin(num1)[2:]
            
    for j, num2 in enumerate(arr2):
        if len(bin(num2)[2:]) != n:
            arr2[j] = '0' * (n - len(bin(num2)[2:])) + bin(num2)[2:]
        else:
            arr2[j] = bin(num2)[2:]
            
    for a1, a2 in zip(arr1, arr2):
        tmp = ''
        for k in range(n):
            if int(a1[k]) + int(a2[k]) == 0:
                tmp += ' '
            else:
                tmp += '#'
        answer.append(tmp)
    return answer


# if 더해서 0이면 공백 else 1