def insertSort(array):

    for i in range(1, len(array)):
        
        n = i
        while (n > 0) and (array[n] < array[n-1]):
            temp = array[n-1]
            array[n-1] = array[n]
            array[n] = temp

            n -= 1

def main():

    inputs = [[5, 4, 2, 1, 3]]

    for input in inputs:
        print(input)
        insertSort(input)
        print(input)

main()