import sys

def stringBalanced(input):
    stack = []
    for x in input:
        if x == '{' or x == '[' or x == '(':
            stack.append(x)

        if x == '}' or x == ']' or x == ')':
            if len(stack) == 0 :
                return False
            if isOpeningAndClosingBracketMatch(stack, x):
                stack.pop()
    if len(stack) == 0:
        print("string {0} is balanced YES".format(input))  
    if len(stack) > 0:
        print("string {0} is NOT balanced".format(input))            
            

def isOpeningAndClosingBracketMatch(stack, closingBracket):
    if stack[0] == '{' and closingBracket == '}':
        return True
    if stack[0] == '[' and closingBracket == ']':
        return True
    if stack[0] == '(' and closingBracket == ')':
        return True
    else:
        return False
       


stringBalanced("[{}{})(]") #unbalanced
stringBalanced("[]") # balanced
stringBalanced(")(") #unbalanced
stringBalanced("()") #balanced
stringBalanced("{[]{()}}")  #balanced   
stringBalanced("((()") #unbalanced           
             
                
    
