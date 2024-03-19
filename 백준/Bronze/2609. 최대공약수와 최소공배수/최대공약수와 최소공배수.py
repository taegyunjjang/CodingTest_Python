from math import gcd
import sys
input = sys.stdin.readline


def solution():
    a, b = map(int, input().split())
    get_gcd = gcd(a, b)
    get_lcm = (a*b)//get_gcd
    
    print(get_gcd)
    print(get_lcm)
    
solution()