def solution(bandage, health, attacks):
    total_time = attacks[-1][0] + 1
    attack_idx, consecutive_success = 0, 0
    casting_time, recovery, additional_recovery = bandage[0], bandage[1], bandage[2]
    max_health = health
    
    for t in range(1, total_time):
        if t == attacks[attack_idx][0]:
            health -= attacks[attack_idx][1]
            
            if health <= 0:
                return -1
            
            attack_idx += 1
            consecutive_success = 0
        else:
            consecutive_success += 1
            
            if consecutive_success == casting_time:
                health += additional_recovery
                consecutive_success = 0
                
            if health < max_health:
                health += recovery
                
            if health > max_health:
                health = max_health
                
    return health