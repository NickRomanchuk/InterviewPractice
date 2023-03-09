def reverseList(array):

    new_array = array[:]

    for i in range(len(array)):
        new_array[(-1*i)-1] = array[i]
    
    return new_array

def main():
    x = [1, 2, 3]
    print(x)
    print(reverseList(x))
    print(x)

main()