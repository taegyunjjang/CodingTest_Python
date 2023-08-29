def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1)  + abs(y2 - y1)

def solution(numbers, hand):
    answer = ''
    leftLocation, rightLocation = (0, 0), (2, 0)
    dic = {
        1 : (0, 3), 2 : (1, 3), 3 : (2, 3),
        4 : (0, 2), 5 : (1, 2), 6 : (2, 2),
        7 : (0, 1), 8 : (1, 1), 9 : (2, 1),
        0 : (1, 0)
    }
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            leftLocation = dic[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            rightLocation = dic[num]
        else:
            if distance(dic[num], leftLocation) > distance(dic[num], rightLocation):
                answer += 'R'
                rightLocation = dic[num]
            elif distance(dic[num], leftLocation) < distance(dic[num], rightLocation):
                answer += 'L'
                leftLocation = dic[num]
            else:
                if hand == 'left':
                    answer += 'L'
                    leftLocation = dic[num]
                else:
                    answer += 'R' 
                    rightLocation = dic[num]
    return answer