def anagram(s1, s2):

    if len(s1) != len(s2):
        return False
    
    for i in s1:
        if i not in s2:
            return False
        else:
            if s1.count(i) != s2.count(i):
                return False
            
    return True

def main():

    inputs = [['abc', 'abb'], ['cinema', 'iceman'], ['cci', 'iic']]

    for input in inputs:

        print("Input: ", input)
        print("Output: ", anagram(input[0], input[1]), '\n')

if __name__ == "__main__":
    main()