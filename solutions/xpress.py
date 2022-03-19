m, n = map(int, input().split())

def solve(arr, m, n, bh):
    steps = [[-1 for i in range(n)] for i in range(m)]
    steps[0][0] = 0
    frontier = [(0, 0)]
    solved = False
    res = -1

    def update(x, y, step):
        nonlocal res
        nonlocal solved
        if x == n-1 and y == m-1:
            res = step
            solved = True
            return 0
        if steps[y][x] == -1:
            steps[y][x] = step
            frontier.append((x, y))
            if arr[y][x] != 0:
                bhs = bh[arr[y][x]]
                for coord in bhs:
                    xx, yy = coord
                    if xx != x and yy != y and steps[yy][xx] == -1:
                        steps[yy][xx] = step
                        frontier.append((xx, yy))

    def next():
        x, y = frontier[0]
        if x - 1 >= 0:
            update(x - 1, y, steps[y][x] + 1)
        if y - 1 >= 0:
            update(x, y - 1, steps[y][x] + 1)
        if x + 1 < n:
            update(x + 1, y, steps[y][x] + 1)
        if y + 1 < m:
            update(x, y + 1, steps[y][x] + 1)
        frontier.pop(0)

    while not solved:
        next()
    return res

arr = []
bh = {}

for i in range(m):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] != 0:
            if row[j] not in bh:
                bh[row[j]] = []
            bh[row[j]].append((j, i))
    arr.append(row)

print(solve(arr, m, n, bh))
