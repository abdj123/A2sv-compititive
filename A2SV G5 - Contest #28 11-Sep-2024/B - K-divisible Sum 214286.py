# Problem: B - K-divisible Sum - https://codeforces.com/gym/540354/problem/B

for _ in range(int(input())):
    n,k = map(int,input().split())
    if n >= k:
        print(1 if n % k == 0 else 2)
    else:
        print((k-1)//n + 1)