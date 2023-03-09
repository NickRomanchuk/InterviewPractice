def findLargeSmall(array):

    maximum = array[0]
    minimum = array[0]

    for x in array:
        if x > maximum:
            maximum = x
        
        if x < minimum:
            minimum = x
    
    return [maximum, minimum]

def main():

    inputs = [[1,3,4,9,2,0,4]]

    for input in inputs:
        print(findLargeSmall(input))

main()