n = int(input())
a = list(map(int, input().split()))

for i in a:
    c = i - min(a)
    print(c, end=' ')