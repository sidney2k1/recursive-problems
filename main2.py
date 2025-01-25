#program to reverse a string
def reversestring(s):
    if len(s)==1:
        return s[0]
    firstchar=s[0]
    return reversestring(s[1:]) + firstchar
s="aayan"
print("Reversed string=",reversestring(s))