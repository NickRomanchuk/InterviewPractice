def reverse(string):
    
    reversed_string = ''

    for i in string:
        reversed_string = i + reversed_string

    return reversed_string

def main():

    inputs = ['Hello']

    for input in inputs:
        print("Input: ", input)
        print("Output: ", reverse(input))

if __name__ == "__main__":
    main()