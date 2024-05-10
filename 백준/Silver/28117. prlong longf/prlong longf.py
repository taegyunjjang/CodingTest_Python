import sys
input = sys.stdin.readline

def ll_to_i(S):
    ll = "longlong"
    cnt = 1
    
    if ll in S:
        idx = S.index(ll)
        new_S = S[:idx] + "int" + S[idx+8:]
        cnt += ll_to_i(new_S) + ll_to_i(S[idx + 4:]) - 1
            
    return cnt
    
def solution():
    N = int(input())
    S = input().rstrip()
    print(ll_to_i(S))
    
            
solution()
