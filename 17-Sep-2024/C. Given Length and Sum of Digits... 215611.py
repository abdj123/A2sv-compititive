# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m, s = map(int, input().split())
st = s
res = []

for i in range(m):
    x = min(9,s)
    res.append(str(x))
    s -= x
mx = int("".join(res))
mn = res[::-1]
if mn[0] == "0":
    for ind in range(len(mn)):
        if mn[ind] != "0":
            mn[ind] = str(int(mn[ind]) - 1)
            break
    mn[0] = "1"
    mn = int("".join(mn))
else:
    mn = int("".join(mn))
if m * 9 < st or (st == 0 and m > 1):
    print(-1, -1)
elif m == 1 and st == 0:
    print(0, 0)
else:
    print(mn, mx)