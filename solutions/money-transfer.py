#!/usr/bin/env python3

N, T = list(map(int, input().split()))

users = {}
for _ in range(N):
    user, money = list(input().split())
    users[user] = int(money)

for _ in range(T):
    a, b, amt = list(input().split())
    amt = int(amt)
    if amt > users[a]:
        continue
    users[a] = users[a] - amt
    users[b] = users[b] + amt

# for k, v in users.items():
    # print(k, v)

for key in sorted(users):
    print(key, users[key])
