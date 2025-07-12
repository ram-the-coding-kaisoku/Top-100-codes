#Brute force method to find the HCF of two numbers

def hcf(a,b):
    for i in range(1,a+1):
        if (a%i==0 and b%i==0):
            factor=i
    return factor

result=hcf(15,30)

print(result)
        