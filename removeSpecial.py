def replaceSpecial(String):

    new_string = ''
    for char in String:
        if char.isalnum():
            new_string += char

    return new_string

def main():

    print(replaceSpecial("Hello!!:)"))

main()