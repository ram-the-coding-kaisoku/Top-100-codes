#Strong Number Program in Python
'''
145 
1! - 1 + 4! 24 +5! 120 = 145 

Algorithm
n
sum=0
n%10 = digit
factorial(digit)
    n>0
    fact =fact * n
    n-1 
fact=+fact
fact == num -> storng number
'''

def factorial(n):
    fact=1
    while n>0:
        fact=fact*n
        n-=1
    return fact

def strong_num(n):
    sum=0
    temp=n
    while temp>0:
        digit = temp % 10
        sum = sum + factorial(digit)
        temp//=10
    if sum==n:
        print(f"{n} is a strong number")
    else:
        print(f"{n} is not a strong number")

n=int(input("Enter the number "))
strong_num(n)
