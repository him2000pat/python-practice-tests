import sys

def reverseString(input):
    lenght = len(input)
    while(lenght > 0):
        print(input[lenght-1])
        lenght = lenght - 1
    

def reverseStringByRecursion(input):
    lenght = len(input)
    print(input[lenght-1])
    if (lenght > 0):
        reverseStringByRecursion(input[0:lenght-1])

print("Reverse string by for loop")
reverseString("India")

print("Reverse string by recursion")
reverseStringByRecursion("Jack")
