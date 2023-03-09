def isPrime(n):
    
    if n <= 1:
        return False
    else:
        for i in range(2, (n // 2) + 1):
            if (n % i) == 0:
                return False

    return True

def main():

    inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for input in inputs:
        print("Input: ", input)
        print("Output: ", isPrime(input))

main()