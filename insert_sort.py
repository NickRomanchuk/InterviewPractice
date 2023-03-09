def insert_sort(array):

    for i in range(1, len(array)):

        n = i
        while (n > 0) and (array[n-1] > array[n]):
            x = array[n]
            array[n] = array[n-1]
            array[n-1] = x
            n -= 1

    return array

def main():

    inputs = [[4, 3, 2, 10, 12, 1, 5, 6]]

    for input in inputs:
        print(insert_sort(input))

if __name__ == "__main__":
    main()                