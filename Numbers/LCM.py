'''
Program to find the LCM of two numbers

4 - 4 8 12 16 20
6 - 6 12 18 24 
4 * 6 = 24 

'''
def lcm(a,b):
    i=a*b
    m=max(a,b)
    factor=0
    count=0
    while i>=m:
        count+=1
        if i%a==0 and i%b==0:
            factor=i
        i-=1
    print(count)
    return factor

result = lcm(2,1024)
print(result)