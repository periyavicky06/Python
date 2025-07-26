s=input("Give the string :")
x=int(input("Give the integer value :"))
front=s[0:-x]
last=s[len(s)-x:]
reverse=last[::-1]
print(front+reverse)
