def solution(babbling):
    answer = 0
    for s in babbling:
        if "aya" in s and "ayaaya" not in s:
            s = s.replace("aya", "1")
        if "ye" in s and "yeye" not in s:
            s = s.replace("ye", "1")
        if "woo" in s and "woowoo" not in s:
            s = s.replace("woo", "1")
        if "ma" in s and "mama" not in s:
            s = s.replace("ma", "1")
        if s.isdigit():
            answer += 1
    return answer