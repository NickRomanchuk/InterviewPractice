def matchingChar(String):
    matching = []

    for i in range(len(String)):
        if (String[i] in String[i+1:]) and (String[i] not in matching):
            matching.append(String[i])

    return matching

def main():

    inputs = ['', 'Nicholas', 'cineme', 'lnnicll']

    for input in inputs:
        print("Input: ", input)
        print("Output: ", matchingChar(input))

main()