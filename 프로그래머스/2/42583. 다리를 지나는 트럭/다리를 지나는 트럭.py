def solution(bridge_length, weight, truck_weights):
    t = 0
    bridge = [0 for i in range(bridge_length)]
    totWeight = 0
    
    for w in truck_weights:
        if totWeight + w <= weight:
            t += 1
            totWeight -= bridge[0]
            bridge = bridge[1:] + [w]
            totWeight += w

        elif totWeight + w > weight:
            while totWeight + w > weight:
                t += 1
                totWeight -= bridge[0] 
                bridge = bridge[1:] + [0]
            bridge[-1] = w
            totWeight += w

        elif len(bridge) == bridge_length:
            if totWeight - bridge[0] + w <= weight:
                totWeight -= bridge[0]
                t += 1
                bridge = bridge[1:] + [w]
                totWeight += w

            else:
                while totWeight + w > weight:
                    t += 1
                    totWeight -= bridge[0] 
                    bridge = bridge[1:] + [0]
                bridge[-1] = w
                totWeight += w
            
            
    while len(bridge) != 0:
        bridge.pop()
        t += 1
        
    return t
            