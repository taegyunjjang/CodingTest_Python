def solution(k, score):
    answer = []
    hallOfFame = []
    for s in score:
        hallOfFame.append(s)
        hallOfFame = sorted(hallOfFame)[::-1][:k]
        answer.append(hallOfFame[-1])
            
    return answer