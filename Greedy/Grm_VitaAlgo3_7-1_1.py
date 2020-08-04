# 7월 1주차 보조 배터리

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
a, b, c = map(int, input().split())
n = int(input())
pin_5 = []
pin_8 = []
cnt = 0
res = 0
for i in range(n):
    cost, pin = map(int, input().split())
    if pin == 0:
        pin_5.append(cost)
    else:
        pin_8.append(cost)

pin_5.sort(reverse=True)
pin_8.sort(reverse=True)

while pin_5 and a != 0:
    res += pin_5.pop()
    a -= 1
    cnt += 1

while pin_8 and b != 0:
    res += pin_8.pop()
    b -= 1
    cnt += 1

while c != 0:
    if pin_5 and pin_8:
        if pin_5[-1] < pin_8[-1]:
            res += pin_5.pop()
            cnt += 1
        else:
            res += pin_8.pop()
            cnt += 1
    elif pin_5 and not pin_8:
        res += pin_5.pop()
        cnt += 1
    elif pin_8 and not pin_5:
        res += pin_8.pop()
        cnt += 1
    c -= 1

print(cnt, res)

