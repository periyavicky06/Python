a=input("Give the string:")
b=[]    
for i in range(len(a)-1,-1,-1):
    c=b.append(a[i])
b=''.join(b)
print(b)
if(a==b):
    print("It is a palindrome")
else:
    print("Not a palindrome")
    
