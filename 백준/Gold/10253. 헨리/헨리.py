import sys
from fractions import Fraction

T = int(sys.stdin.readline())

def henry(numer, denom):
    if numer == 1:
        return denom
    else:
        x = (denom // numer) + 1
        step = Fraction(numer, denom) - Fraction(1, x)
        return henry(step.numerator, step.denominator)
    
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(henry(a, b))