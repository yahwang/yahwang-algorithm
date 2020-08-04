# 5월 2주차 가즈아

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, k = map(int, input().split())
days = [int(i) for i in input().split()]
coins = 0
total = k
low = days[0]
for idx, day in enumerate(days[1:], start=1):
    low = min(low, days[idx - 1])
    coins = k // low
    total = max(total, coins * day + (k % low))

print(total)
