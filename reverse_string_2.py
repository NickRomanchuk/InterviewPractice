def Reverse(String):

    new_string = ''

    for char in String:
        new_string = char + new_string

    return new_string

def main():
    print("Input: ", "Hello")
    print("Output: ", Reverse("Hello"))

if __name__ == "__main__":
    main()