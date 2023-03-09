def repeatedElements(array):
    
    new_array = []

    for x in array:
        if array.count(x) <= 1:
            new_array.append(x)

    return new_array
    
def main():

    inputs = [[1, 2, 3, 2, 4]]

    for input in inputs:
        print(input)
        print(repeatedElements(input))
        print(input)

main()
