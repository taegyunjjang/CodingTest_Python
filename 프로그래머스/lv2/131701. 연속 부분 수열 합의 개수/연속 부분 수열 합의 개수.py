def solution(elements):
    l = len(elements)
    s = {num for num in elements}
    for i in range(l - 2):
        elements.append(elements[i])
        
    for j in range(2, l):
        for k in range(l):
            s.add(sum(elements[k:k + j]))
    return len(s) + 1