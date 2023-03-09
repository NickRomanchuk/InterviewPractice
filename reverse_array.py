def reverse_array(array):

    new_array = []

    for element in array:

        new_array.insert(0, element)
    
    return new_array

def main():

    print(reverse_array(['a', 'b', 'c']))

main()