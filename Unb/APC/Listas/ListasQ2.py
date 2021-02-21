n = int(input())
a = list(map(int, input().split()))

for i in a:
    c = max(a) - i
    print(c, end=' ')
