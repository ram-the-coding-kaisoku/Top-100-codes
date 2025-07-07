#Perfect Number in Python
'''
Perfect Number
A Number that can be represented as the sum of all the factors of the number is known as a Perfect Number.
Let's Try and understand it better using an example

Example
Input : 28
Output : It's a Perfect Number
Explanation : Number = 28
28 = 1 + 2 + 14 + 4 + 7
as the number 28 has factors 1, 2, 4, 7 and 14.

'''


def perfect_number(n):
    sum=0
    for i in range(1,(n//2 + 1)):
        if n%i==0:
            sum+=i
    if n==sum:
        print(f"{n} is perfect number")
    else:
        print(f"{n} is not a perfect number")
        
#pilot code
n=int(input("Enter the number "))
perfect_number(n)