def isPalidrome(String):
    
    for i in range(len(String)):
        if String[i] != String[(-1*i)-1]:
            return False

    return True

def main():
    inputs = ['Hello', 'World', '', 'a', 'helleh']

    for input in inputs:

        print("Input: ", input)
        print("Output: ", isPalidrome(input), '\n')

main()