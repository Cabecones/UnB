def count_0s(x):
    x = bin(x)
    return(x.count('0'))-1

print(count_0s(323))