def solution(myString, pat):
    lenPat = len(pat)
       
    return myString[:lenPat + myString.rfind(pat)]