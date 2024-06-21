import sys
input = sys.stdin.readline

class Set:
    def __init__(self):
        self.s = set()
    
    def add(self, x):
        if x not in self.s:
            self.s.add(x)
    
    def remove(self, x):
        if x in self.s:
            self.s.remove(x)
            
    def check(self, x):
        if x in self.s:
            print(1)
        else:
            print(0)
    
    def toggle(self, x):
        if x in self.s:
            self.remove(x)
        else:
            self.add(x)
            
    def all(self):
        self.s = set([i for i in range(1, 21)])
    
    def empty(self):
        self.s.clear()


def solution():
    M = int(input())
    S = Set()
    
    for _ in range(M):
        op = input().rstrip()
        if op == 'all' or op == 'empty':
            getattr(S, op)()
        else:
            op, x = op.split()
            x = int(x)
            getattr(S,op)(x)
            
            
solution()