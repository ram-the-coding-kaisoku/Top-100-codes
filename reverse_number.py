#Reverse a Number in Python
'''
Find the Reverse of a Number in Python Language
We need to write a python code to reverse the given integer and print the integer. 
The typical method is to use modulo and divide operators to break down the number and reassemble again in the reverse order. 


1234
digit n % 10 
4 3 2 1
4 * 10 ** 1 + 3 * 10 ** 1 + 2 * 10 ** 2 + 1 * 10 ** 3 
get a number count


'''

#Brute force method
# To get the count of the number
def countnum(num):
    count=0
    while num != 0:
        count+=1
        num//=10
    return count

#Reverse a number

def reverse(n):
    count=int(countnum(n)) - 1
    reverse=0
    while n!=0:
        digit = n % 10
        reverse += digit * (10 ** count)
        count-=1
        n//=10
    return reverse

#pilot
n = int(input("Enter the number "))
result = reverse(n)
print(f"Reverse number of {n} is {result}")

        