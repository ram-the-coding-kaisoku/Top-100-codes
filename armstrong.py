'''

Check Whether a Given Number is an Armstrong Number or Not
Given an integer input, the objective is to check whether or not the given input variable is an Armstrong number. 
In order to do so, we check whether the sum of the digits of each number to the power the length of the number is equal to the number itself or not. If the number is the same as the original, it’s an Armstrong number. 

153
153 % 10 = 3

153 //= 10

get count()

count=0



'''
#Iterative method
#Function to count the digits of a number

def count(num):
    count=0
    while num!=0:
        count+=1
        num//=10
    return count

#function to check if a given number is armstrong or not 
def arm(num):
    exp=count(num)
    temp = num
    sum=0
    while temp!=0:
        digit=temp%10
        sum=sum+(digit**exp)
        temp//=10
    if sum==num:
        return f"{num} is an armstrong number"
    else:
        return f"{num} is not an armstrong number"
    
    
#Pilot code
n=int(input("Enter the number"))
print(arm(n))

#Recursive method yet to be done