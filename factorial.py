#Factorial of a Number in Python
'''
factorial of a number is multiples of the numbers below them eg
5! = 5 x 4!
         4 x 3!

or 5! = 5 4 3 2 1

Algorithm
get n
fact = 1
loop while n>0:
    fact= fact * n
    n = n-1
return fact

'''
#Function to get factorial of a number
def factorial(n):
    fact=1
    while n>0:
        fact*=n
        n-=1
    return fact


#pilot code
n=int(input("Enter the number "))
print(factorial(n))