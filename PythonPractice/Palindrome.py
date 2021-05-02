def palindrome(input):
    if input is None:
        return None
    if len(input) == 1:
        return "Not a valid input"
    
    revStr = reverse(input)
    if(input == revStr):
        print("{0} is Palindrome".format(input))
    else:
        print("{0} is Not Palindrome".format(input))    

def reverse(input):
#    consider we are passing the valid value
    length = len(input) - 1
    reverseString = ""
    while(length >= 0):
        reverseString = reverseString + input[length]
        length = length - 1
    return reverseString            
        
palindrome("madam")
palindrome("Level") 
palindrome("LEVEL") 
palindrome("saippuakivikauppias")      