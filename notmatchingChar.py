def nonmatchingChar(String):
    
    matching = {}
    for i in range(len(String)):
        if (String[i] in matching.keys()):
            matching[String[i]] += 1
        else:
            matching[String[i]] = 1

    return [x for x in matching.keys() if matching[x] == 1]

def main():

    inputs = ['lnnicll']

    for input in inputs:
        print("Input: ", input)
        print("Output: ", nonmatchingChar(input))

main()