def factorial(n):

    fact = 1
    for i in range(1, n + 1):
        fact *= i
    
    return fact

def main():

    inputs = [0, 1, 5]

    for input in inputs:
        print("Input: ", input)
        print("Output :", factorial(input))

main()