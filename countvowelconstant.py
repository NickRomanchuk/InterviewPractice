def countVowelsConst(String):
    vowels = ['a', 'e', 'i', 'o', 'u']

    vowel_count = 0
    const_count = 0
    for char in String:
        if char.lower() in vowels:
            vowel_count += 1
        else:
            const_count += 1

    return vowel_count, const_count

def main():

    inputs = ['Apple', 'hello', 'School']

    for input in inputs:
        print("Input: ", input)
        print("Output: ", countVowelsConst(input))

if __name__ == "__main__":
    main()