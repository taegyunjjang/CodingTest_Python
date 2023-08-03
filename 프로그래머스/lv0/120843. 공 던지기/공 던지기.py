def solution(numbers, k):
    l = len(numbers)
    if l % 2 == 0:
        return numbers[2 * (k % (l // 2) - 1)]
    else:
        if (k % l) > (l + 1) // 2:
            return numbers[2 * ((k % l) - ((l + 1) // 2)) - 1]
        else:
            return numbers[2 * (k % l - 1)]
    
    # [1,2,3,4,5,6,7], k=6
    # 1, 3, 5
    # 0, 2, 4, 6