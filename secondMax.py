def secondMax(array):

    maximum = max(array)
    second = min(array)

    for x in array:
        if (x > second) and (x < maximum):
            second = x
    
    return second

def main():

    inputs = [[1,2,3], [1,6,5,4,2],[1,5,6,4,6]]

    for input in inputs:
        print(secondMax(input))

main()
