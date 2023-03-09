def palidrome(string):

    mid = len(string) // 2

    for i in range(mid):
        if string[i] != string[(-1*i)-1]:
            return False
        
    return True

def main():

    inputs = ['ABC', 'ABA']

    for input in inputs:
        print("Input: ", input)
        print("Output: ", palidrome(input))

if __name__ == "__main__":
    main()