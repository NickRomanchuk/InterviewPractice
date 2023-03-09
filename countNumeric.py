def countNumeric(String):

    count = 0
    for char in String:
        if char.isnumeric():
            count += 1
    
    return count

def main():

    inputs = ['ABCDE', '', '1', 'Abc2r4']

    for input in inputs:

        print('Input: ', input)
        print('Output: ', countNumeric(input))

if __name__ == "__main__":
    main()
