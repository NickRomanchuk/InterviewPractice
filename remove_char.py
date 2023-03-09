def remove_char(string, char):

    new_string = ''

    for i in string:
        if i != char:
            new_string += i

    return new_string

def main():

    inputs = ['abc', 'aaa', 'bcd']

    for input in inputs:

        print("Input: ", input)
        print("Output: ", remove_char(input, 'a'), '\n')

if __name__ == "__main__":
    main()