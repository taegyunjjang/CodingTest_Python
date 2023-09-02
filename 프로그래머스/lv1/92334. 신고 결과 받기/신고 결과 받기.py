def solution(id_list, report, k):
    reported = {user_id : 0 for user_id in id_list}
    userDic = {user_id : 0 for user_id in id_list}
    
    # 유저의 신고당한 횟수
    for r in set(report):
        reported[r.split()[1]] += 1
    
    # k번 이상 신고당한 유저를 신고한 유저
    for r in set(report):
        user, reportedUser = r.split()
        if reported[reportedUser] >= k:
            userDic[user] += 1
    
    return list(userDic.values())
