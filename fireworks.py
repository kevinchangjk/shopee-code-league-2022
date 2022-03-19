n, m, d = map(int, input().split())
times = []
arr = []

for i in range(m):
    a, b, t = map(int, input().split())
    if b == 0:
        continue
    if t not in times:
        times.append(t)
        arr.append([0 for r in range(n)])
        if len(times) > 1:
            maxd = d * (times[-1] - times[-2])
            maxel = -1
            for x in range(n):
                if maxel == -1 or (x - maxd - 1 >= 0 and arr[-2][x - maxd - 1] == maxel):
                    start = max(0, x - maxd)
                    maxel = max(arr[-2][start:end])
                elif x + maxd < n and arr[-2][x + maxd] > maxel:
                    maxel = arr[-2][x + maxd]
                arr[-1][x] += maxel
    for x in range(n):
        arr[-1][x] += (b - abs(a - (x + 1)))

print(max(arr[-1]))
