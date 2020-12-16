n = int(input())
k = '21'
if n == 1:
    print(1)
elif n == 2:
    print("1\n11")
elif n == 3:
    print("1\n11\n21")
else:
    print("1\n11\n21")
    for i in range(3, n):
        schet = 1
        p = ''
        for j in range(1, len(k)):
            if k[j - 1] == k[j]:
                schet += 1
            else:
                p += str(schet) + k[j - 1]
                schet = 1
        p += str(schet) + k[-1]
        print(p)
        k = p[:]