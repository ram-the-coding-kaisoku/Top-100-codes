'''
Check Whether or Not the Number is a Palindrome in Python Language
A Palindrome Number in Python is a number that remains the same when its digits are reversed. 
In simple terms, if you read the number forward or backward, it looks the same.

'''

#Brute Force


# Function to check if a number is palindrome or not

def Palindrome(n):
    num = n
    reverse=0
    while n !=0:
        digit = n % 10
        reverse = (reverse*10) + digit
        n//=10
    #check the if the number is palindrome or not 
    print(reverse)
    if reverse == num:
        return f"{num} is a palindrome number"
    else:
        return f"{num} is not a palindrome number"
    
    
n = int(input("Enter the number "))
print(Palindrome(n))
    
    