def sum(int_array):

    sum = 0

    for i in int_array:
        sum += i

    return sum

def main():

    inputs  = [[1, 2, 3, 4, 5]]

    for input in inputs:

        print("Input: ", input)
        print("Output: ", sum(input))

if __name__ == "__main__":
    main()