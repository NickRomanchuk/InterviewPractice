def bubbleSort(array):

    for i in range(len(array) - 1):

        for j in range(len(array) - 1 - i):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp

def main():

    inputs = [[5, 4, 1, 6, 2, 3]]

    for input in inputs:
        print(input)
        bubbleSort(input)
        print(input)

main()