def solution(people, limit):
    cnt = len(people)
    i, j = 0, len(people) - 1
    people.sort()
    while i < j:
        if people[i] + people[j] > limit:
            j -= 1
        else:
            cnt -= 1
            i += 1
            j -= 1
    return cnt