def solution(array, height):
    array.append(height)
    array.sort()
    for i, num in enumerate(reversed(array)):
        if num == height:
            return i