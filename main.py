#program to reverse numbers using recursion
def reversenumber(num):
    if num>0:
        #if the input number is not 0 then get the last digit and add it the current reversed number
        last=num%10
        if num//10>0:
            currentnumber=reversenumber((int)(num//10))
            return last*pow(10,len(str(currentnumber)))+currentnumber
        return num
num=int(input("Enter a number:"))
print("reversed:",reversenumber(num))

    