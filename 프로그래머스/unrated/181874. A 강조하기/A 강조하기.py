def solution(myString):
    result = ''
    for char in myString:
        if char == 'a':
            result += 'A'
        elif char != 'A' and char.isupper():
            result += char.lower()
        else:
            result += char
    return result