def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print(f'Mover de {fp} para {tp}.')

num, A, B, C = map(str, input().split())


moveTower(int(num), A, B, C)