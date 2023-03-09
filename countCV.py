def countCV(String):

    vowels = ['a','e','i', 'o', 'u']

    count_v = 0
    count_c = 0
    for char in String:
        if char in vowels:
            count_v += 1
        else:
            count_c += 1
    
    return [count_v, count_c]

def main():
    
    print(countCV("Nicholas"))

main()