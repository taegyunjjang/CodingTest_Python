def solution(n, lost, reserve):
    student = [1 if i not in lost else 0 for i in range(1, n + 1)]
    for r in reserve:
        student[r - 1] += 1
    
    for i, s in enumerate(student):
        if s == 0:
            if i == 0 and student[i + 1] == 2:
                student[i], student[i + 1] = 1, 1
            elif i == len(student) - 1 and student[i - 1] == 2:
                student[i], student[i - 1] = 1, 1
            elif i != 0 and i != len(student) - 1:
                if student[i - 1] == 2:
                    student[i], student[i - 1] = 1, 1
                elif student[i + 1] == 2:
                    student[i], student[i + 1] = 1, 1
    
    return n - student.count(0)