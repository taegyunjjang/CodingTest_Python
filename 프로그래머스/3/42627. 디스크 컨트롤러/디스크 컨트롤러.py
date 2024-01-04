def solution(jobs):
    jobs.sort(key=lambda x: x[1])
    total_time = 0
    current_time = 0
    jobs_len = len(jobs)
    
    while len(jobs) != 0:
        for i in range(len(jobs)):
            request_time, execution_time = jobs[i]
            
            # 현재 시점에 처리할 수 있는 작업
            if current_time >= request_time:
                total_time += current_time + execution_time - request_time
                current_time += execution_time
                jobs.pop(i)
                break
                
            # 현재 시점에 처리할 수 있는 작업이 없으면 현재 시점 증가 
            if i == len(jobs) - 1:
                current_time += 1
    
    return total_time // jobs_len
