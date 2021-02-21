def count_1s(x):
    x = bin(x)
    return(x.count('1'))-1

print(count_1s(6))

