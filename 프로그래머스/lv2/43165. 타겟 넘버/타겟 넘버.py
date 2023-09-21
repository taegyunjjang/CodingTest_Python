def solution(numbers, target):
    nodes = [0]
    for num in numbers:
        tmp = []
        for node in nodes:
            tmp.append(node + num)
            tmp.append(node - num)
        nodes = tmp
    
    return nodes.count(target)