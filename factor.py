# Find factors of a number in python

"""
Algorithm
n
1,n/2 +1
n%i==0
print(i)


"""

def factors(n):
    for i in range(1,(n//2)+1):
        if n%i==0:
            print(f"{i} ",end="")

#pilot code
n = int(input("Enter the number"))
factors(n)