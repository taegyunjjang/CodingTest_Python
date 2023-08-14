def solution(sizes):
    M1, M2 = 0, 0
    for i in range(len(sizes)):
        sizes[i].sort(reverse=True)
    for i in range(len(sizes)):
        if M1 < sizes[i][0]:
            M1 = sizes[i][0]
        if M2 < sizes[i][1]:
            M2 = sizes[i][1]
    return M1 * M2