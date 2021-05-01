import sys

def reverseString(input):
    print(input)
 
def main(): 
    reverseString("This is moudle A")
print("value of __name__ is: {}".format( __name__))

if __name__ == "__main__":
    main()
    
print("Part of the Module A Outside of main function")    
    
    
 #This module A and module B explains the the use of __name__ variable.
 #We have a file A (module A) - having a main function along with the condition (if __name__ == __main__ ). 
 # When we call the file A using the terminal or in VS Code, the main function will be called,
 # because __name__ will be equal to string __main__.  We have a module B and that imports the module A, 
 # if you run the module B, it will not call the main function of module A. 
 # Because the value of __name__ is now module B  __name__ condition helps to run python module as 
 # independent or reusable    
 # you can more information - https://www.guru99.com/learn-python-main-function-with-examples-understand-main.html