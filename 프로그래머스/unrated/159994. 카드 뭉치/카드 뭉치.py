def solution(cards1, cards2, goal):
    for s in goal:
        if s in cards1:
            if cards1[0] != s:
                return "No"
            else:
                cards1 = cards1[1:]
        else:
            if cards2[0] != s:
                return "No"
            else:
                cards2 = cards2[1:]    
    return "Yes"