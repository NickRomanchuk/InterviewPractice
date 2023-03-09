def matching_elements(array):

    new_array = []

    range(0, 10, 1)
    range(0, 10)

    for i in range(len(array) - 1):

            if (array[i] in array[i+1:]) and (array[i] not in new_array):
                new_array.append(array[i])

    return new_array


def main():

    inputs = [[1, 2, 5], [1, 1, 2, 3, 3, 4], [1, 2, 1, 3, 1, 2], [1,1,1,1,1,1,1], [1,1]]

    for input in inputs:
        print(matching_elements(input))

main()