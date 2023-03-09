def bubble_sort(array):

    for i in range(len(array)-1):

        for j in range(len(array) - i - 1):

            if array[j] > array[j+1]:
                x = array[j+1]
                array[j+1] = array[j]
                array[j] = x

    return array

def main():

    inputs = [[5, 4, 1, 2, 3], [2, 5, 3, 7, 1, 9, 1]]

    for input in inputs:
        print("Input: ", input)
        print("Output: ", bubble_sort(input))

main()