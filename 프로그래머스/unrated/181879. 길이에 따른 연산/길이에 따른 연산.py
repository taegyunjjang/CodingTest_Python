def solution(num_list):
    answer = 0
    sum = 0 
    mul = 1
    if len(num_list) > 10:
        for num in num_list:
            sum += num
        return sum
    else:
        for num in num_list:
            mul *= num
        return mul