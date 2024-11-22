# Problem: D - Decide Your Division - https://codeforces.com/gym/543431/problem/D

t = int(input())

for _ in range(t):
    n = int(input())
    two = three = five = 0

    while n % 2 == 0:
        n //= 2
        two += 1

    while n % 3 == 0:
        n //= 3
        three += 1

    while n % 5 == 0:
        n //= 5
        five += 1
        
    if n != 1:
        print(-1)
    else:
        print(two + 2 * three + 3 * five)
    

