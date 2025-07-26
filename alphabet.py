s=input("Give the string :")
x=int(input("Give the finding interger :"))
a=("abcdefghijklmnopqrstuvwxyz")
for i in range(len(s)):
    if(s[i]==a[x-1]):
        print("Yes")
        break
else:
    print("No")