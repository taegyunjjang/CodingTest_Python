def solution(chicken):
    cnt = 0
    while True:
        if chicken < 10:
            break
        tmp = chicken // 10
        cnt += tmp
        chicken = tmp + chicken % 10

    return cnt