
def second_large(array):
    maximum = max(array)
    second = min(array)

    for x in array:
        if (x < maximum) and (x > second):
            second = x
    
    return second

def main():

    inputs = [[1, 2, 3], [1, 4, 3, 4], [1, 3], [7,3,2]]

    for input in inputs:
        print(second_large(input))

main()