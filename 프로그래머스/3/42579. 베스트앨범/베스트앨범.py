def solution(genres, plays):
    # 딕셔너리 초기화
    dic = {genre:[] for genre in set(genres)}

    # 딕셔너리에 (재생수, 인덱스)를 튜플로 넣음
    for i, genre in enumerate(genres):
        dic[genre].append((plays[i], i))
    
    # recordList에 딕셔너리의 value를 넣고, 많이 재생된 장르순으로 정렬
    recordList = []
    for genre in dic:
        recordList.append((dic[genre]))
    recordList.sort(key=lambda x: -sum(y[0] for y in x))
    

    # 정렬된 리스트에서 많이 재생된 노래순으로 정렬
    for i, record in enumerate(recordList):
        record.sort(key=lambda x: (-x[0], x[1]))
    print(recordList)
    
    # answer에 들어갈 노래의 고유 번호 추출 과정
    answer = []
    for record in recordList:
        if len(record) == 1:
            answer.append(record[0][1])
        else:
            answer.append(record[0][1])
            answer.append(record[1][1])
    return answer