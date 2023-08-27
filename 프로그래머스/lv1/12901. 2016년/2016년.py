def solution(a, b):
    answer = ''
    day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    if a in [1, 4, 7]:
        answer = day[(b + 4) % 7]
    elif a in [2, 8]:
        answer = day[b % 7]
    elif a in [3, 11]:
        answer = day[(b + 1) % 7]
    elif a in [5]:
        answer = day[(b + 6) % 7]
    elif a in [6]:
        answer = day[(b + 2) % 7]
    elif a in [9, 12]:
        answer = day[(b + 3) % 7]
    elif a in [10]:
        answer = day[(b + 5) % 7]
    
    return answer

# 1, 3, 5, 7, 8, 10, 12 : 31 
# 2 : 29
# 4, 6, 9, 11 : 30