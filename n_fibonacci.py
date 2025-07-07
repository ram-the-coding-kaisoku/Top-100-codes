#Find the Nth Term of a Fibonacci Series in Python
'''
Algorithm:
0 1 1 2 3 5 8 13 21 34 55

itialize f0=0 f1= 1 f2=0
start loop 2,n+1
    f2 = f0+f1
    f0=f1
    f1=f2
return the f2

'''

def n_fibonacci(n):
    f0=f2=0
    f1=1
    for i in range(2,n+1):
        f2=f0+f1
        f0=f1
        f1=f2
    return f2

#pilot code
n=int(input("Enter the number "))
print(n_fibonacci(n))