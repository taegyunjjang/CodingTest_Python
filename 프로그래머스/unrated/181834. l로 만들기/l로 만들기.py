def solution(myString):
    newString = ""
    for char in myString:
        if 'a' <= char <= 'k':
            newString += 'l'
        else:
            newString += char
    return newString