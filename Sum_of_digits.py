'''
Find the sum of the Digits of a Number
Given a number as an input the objective is to calculate the sum of the digits of the number. We first break down the number into digits and then add all the digits to the sum variable. We use the following operators to break down the string,

Modulo operator %: We use this operator to extract the digits from the number.
Divide operator /: We use this operator to shorten the number after the digit has been extracted.

'''
'''
8974

4 + 7 + 9 + 8

while num > 0
sum = 0
num % 10 = val
sum+=value
num // 10

'''

#Function to find the sum of digits in brute force

def sum_of_digits_bf(num):
    sum = 0
    while num > 0:
        last = num % 10
        sum+=last
        num//=10
    return sum

#Function to find the sum of digits in recursion

def sum_of_digits_rec(n,sum):
    if n==0:
        return sum
    else:
        sum += n % 10
        return sum_of_digits_rec(n//10,sum)
               
#pilot

n = int(input("Enter the number "))
result=sum_of_digits_rec(n,sum=0)
print(f"The sum of the digits of {n} is {result}")
