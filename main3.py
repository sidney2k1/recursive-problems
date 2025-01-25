#program to check the power of 4
n=int(input("Enter a number to check for power of 4:"))
def checkpower(n):
    if n<=0:
        return False
    elif n==1:
        return True
    elif n%4==0:
        return checkpower(n/4)
    return False
if checkpower(n):
    print(n,"is a power of four")
else:
    print(n,"Is not a power of 4")