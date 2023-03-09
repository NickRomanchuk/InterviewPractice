def bin_search(array, n):
    
    maximum = len(array)
    minimum = 0

    while maximum >= minimum:
        mid = (maximum + minimum) // 2

        if array[mid] < n:
            minimum = mid + 1
        elif array[mid] > n:
            maximum = mid - 1 
        else:
            return mid
    
    return "DNE"

def main():

    inputs = [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4], [1, 2, 3, 5, 6, 7], [1, 2, 3, 4, 5, 6]]

    for input in inputs:
        print("Input: ", input)
        print("Output: ", bin_search(input, 4))

main()