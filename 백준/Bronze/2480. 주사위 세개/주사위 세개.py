l = list(map(int, input().split()))

if len(set(l)) == 1:
    print(10000 + l[0] * 1000)
elif len(set(l)) == 2:
    if l.count(l[0]) == 2:
        print(1000 + l[0] * 100)
    else:
        print(1000 + l[1] * 100)
else:
    print(max(l) * 100)