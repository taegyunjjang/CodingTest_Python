def solution(n):
    for i in range(min(n, 6), 0, -1):
        if n % i == 0 and 6 % i == 0:
            return (6 * n // i) // 6
            
    
# lcm(6, 10) = 30
# lcm(6, 4) = 12
# lcm(6, n) // 6 = 6 * n // gcd(6, n)


