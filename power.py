#Python Program to find Power of a number
'''
2 3
2 2 2

2 ** 3

'''

def power(b,e):
    r=b**e
    return r
#pilot code
b=int(input("base "))
e=int(input("exponent "))
print(power(b,e))