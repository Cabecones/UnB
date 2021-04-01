def fibonacci(n):
    last = 1
    pelast = 1
    if (n==1) or (n==2):
        return("1")
    elif n==0:
        return("0")
    else:
        for count in range(2, n):
            number = last + pelast
            pelast = last
            last = number
            count += 1
        return(number)
fibonacci(10)