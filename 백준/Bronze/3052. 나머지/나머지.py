import sys
input = sys.stdin.readline

def solution():
    residue_list = []
    for _ in range(10):
        residue_list.append(int(input())%42)
    print(len(set(residue_list)))
    
solution()