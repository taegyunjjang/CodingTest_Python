def solution(hp):
    cnt = hp // 5
    hp -= 5 * (hp // 5)
    cnt += hp // 3
    hp -= 3 * (hp // 3)
    cnt += hp
    return cnt