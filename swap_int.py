def swapInt(a, b):
    b = a + b
    
    a = b - a
    b = b -a

    return a, b

def main():

    inputs = [[10, 20], [15, 52]]

    for input in inputs:
        print("Input: ", input)
        print("Output: ", swapInt(input[0], input[1]))

main()