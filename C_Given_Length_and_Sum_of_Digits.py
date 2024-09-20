n, m = map(int, input().split())
if (m == 0 and n > 1) or m > 9*n:
    print(-1, -1)

else:
    mini = [0] * n
    maxi = [0] * n
    mini[0] = 1
    k = m - 1
    for i in range(n-1, -1, -1):
        mini[i] += min(9, k)
        k -= mini[i]

    for i in range(n):
        maxi[i] = min(9, m)
        m -= maxi[i]

    print(''.join(map(str, mini)), ''.join(map(str, maxi)))