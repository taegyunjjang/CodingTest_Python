def solution(price, money, count):
    tot = 0 
    
    for i in range(1, count + 1):
        tot += price * i
    
    if money - tot < 0:
        return tot - money
    else:
        return 0
    
    