def Fibonacci(n):

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def main():

    for i in range(1, 11):
        print(Fibonacci(i))

main()