def FizzBuzz(array):

    for i, value in enumerate(array):

        if (value % 3 == 0) and (value % 5 == 0):
            array[i] = 'fizzbuzz'
        elif (value % 3 == 0):
            array[i] = 'fizz'
        elif (value % 5 == 0):
            array[i] = 'buzz'
    
    return array

def main():

    print(FizzBuzz([3, 4, 15, 5]))

main()
