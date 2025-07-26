a=input("Give the name:")#mom
i=0
while(i<len(a)):
    if a[i] !=a[len(a)-i-1]:# m!=o
        break
    i=i+1
if(i==len(a)):
    print("It is a palindrome")
else:
    print("Not a palindrome")