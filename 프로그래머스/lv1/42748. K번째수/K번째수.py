def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        j, k, l = commands[i]
        answer.append(sorted(array[j - 1:k])[l - 1])
    return answer