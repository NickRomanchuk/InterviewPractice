def count(string, char):

    x = string.count(char)

    return x

def main():

    inputs = ['AAba', 'AACD', 'aaaa']

    for input in inputs:

        print("Input: ", input)
        print("Output: ", count(input, 'a'), '\n')

if __name__ == "__main__":
    main()