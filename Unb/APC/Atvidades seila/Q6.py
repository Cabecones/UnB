import math


def distancia(x1, x2, y1, y2):
    sub1 = x2-x1
    sub2 = y2-y1
    quad1 = sub1**2
    quad2 = sub2**2
    distancia_bola = math.sqrt(quad1+quad2)
    return distancia_bola


x1, x2 = input().split()
x1 = float(x1)
x2 = float(x2)

ax1, ax2 = input().split()
ax1 = float(ax1)
ax2 = float(ax2)
ax = distancia(x1, x2, ax1, ax2)

bx1, bx2 = input().split()
bx1 = float(bx1)
bx2 = float(bx2)
bx = distancia(x1, x2, bx1, bx2)

cx1, cx2 = input().split()
cx1 = float(cx1)
cx2 = float(cx2)
cx = distancia(x1, x2, cx1, cx2)

if ax < bx and ax < cx:
    print(1)
elif bx < ax and bx < cx:
    print(2)
elif cx < ax and cx < bx:
    print(3)
