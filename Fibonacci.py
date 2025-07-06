'''
Find the Fibonacci Series up to Nth Term in Python
Given an integer as an input, the objective is to find the Fibonacci series until the number input as the Nth term.
Therefore, we write a program to Find the Fibonacci Series up to Nth Term in Python Language.


f0 =0
f1 =1
f2 = f0 + f1


'''

#Iterative method
#Function to return fibonacci series upto n term
def fibonacci(n):
    f0=0
    f1=1
    f2=0
    i=1
    print("0 1 ",end="")
    while i < n-1:
        f2=f0+f1
        print(f"{f2} ",end="")
        f0=f1
        f1=f2
        i+=1    

fibonacci(15)