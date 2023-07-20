def solution(order):
    cost = 0
    for coffee in order:
        if "americano" in coffee or "anything" in coffee:
            cost += 4500
        elif "cafelatte" in coffee:
            cost += 5000
    return cost