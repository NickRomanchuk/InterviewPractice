def fibo(n):

    if n == 1:
        x = [0]
    elif n == 2:
        x = [0, 1]
    else:
        x = [0, 1]
        for i in range(2, n):
            x.append(x[i-1] + x[i-2])
    
    return x[-1]

def main():

    print(fibo(58))

main()