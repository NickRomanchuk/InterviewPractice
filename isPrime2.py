def isPrime(n):

    if n < 2:
        return False
    else:
        for i in range(2, (n // 2) + 1):
            if (n % i == 0):
                return False
    
    return True

def main():

    for i in range(14):
        print('Number:', i, 'isPrime:', isPrime(i))

if __name__ == "__main__":
    main()
