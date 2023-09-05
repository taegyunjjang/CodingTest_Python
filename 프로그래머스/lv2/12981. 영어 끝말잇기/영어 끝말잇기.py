def solution(n, words):
    wordsList = []
    isWrong = False
    
    for i, word in enumerate(words):
        if word in wordsList:
            isWrong = True
        else:
            if len(wordsList) != 0:
                if word[0] != wordsList[-1][-1]:
                    isWrong = True
                else:
                    wordsList.append(word)
            else:
                wordsList.append(word)        
        if isWrong:
            return [i % n + 1, i // n + 1]
            
    return [0, 0]