def firstUnique(String):

    for char in String:
        if String.lower().count(char.lower()) == 1:
            return char

    return ''

def main():

    inputs = ['Hello', 'People']

    for input in inputs:
        print(firstUnique(input))

main()