import sys


class Deque():
    def __init__(self):
        self.__list = []
        self.__size = 0

    def push_front(self, x):
        self.__list.insert(0, x)
        self.__size += 1

    def push_back(self, x):
        self.__list.append(x)
        self.__size += 1

    def pop_front(self):
        if self.__size != 0:
            print(self.__list.pop(0))
            self.__size -= 1
        else:
            print(-1)

    def pop_back(self):
        if self.__size != 0:
            print(self.__list.pop())
            self.__size -= 1
        else:
            print(-1)

    def size(self):
        print(self.__size)

    def empty(self):
        if self.__size == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if self.__size != 0:
            print(self.__list[0])
        else:
            print(-1)

    def back(self):
        if self.__size != 0:
            print(self.__list[-1])
        else:
            print(-1)



input = sys.stdin.readline
N = int(input())

dq = Deque()

for _ in range(N):
    S = input().rstrip()

    # push
    if len(S) > 9:
        command, x = S.split()

        if command == "push_back":
            dq.push_back(int(x))
        else:
            dq.push_front(int(x))
    # other
    else:
        if S == "pop_front":
            dq.pop_front()
        elif S == "pop_back":
            dq.pop_back()
        elif S == "size":
            dq.size()
        elif S == "empty":
            dq.empty()
        elif S == "front":
            dq.front()
        else:
            dq.back()