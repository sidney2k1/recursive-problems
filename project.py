n=int(input("Enter a number to check power of 2:"))
def checkpower(n):
    if n<=0:
        return False
    elif n==1:
        return True
    elif n%2==0:
        return checkpower(n/2)
    return False
if checkpower(n):
    print(n,"is a power of 2")
else:
    print(n,"is not a power of 2")