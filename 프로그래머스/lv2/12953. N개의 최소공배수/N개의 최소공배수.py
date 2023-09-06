import math

def solution(arr):
    answer = 1
    for num in arr:
        if num % answer == 0:
            answer = num
        else:
            if math.gcd(answer, num) == 1:
                answer *= num
            else:
                for n in range(1, answer * num + 1):
                    if n % answer == 0 and n % num == 0:
                        answer = n
                        break
    return answer