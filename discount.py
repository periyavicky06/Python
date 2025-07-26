a=int(input("Give the first price :"))
b=int(input("Give the second price :"))
c=int(input("Give the third price :"))
if(b==c):
    res=(b+c)*0.9
    print( round((res+a,2)))
elif(a==b):
    res=(a+b)*0.9
    print(res+c)
elif(a==c):
    res=(a+c)*0.9
    print(res+b)
else:
    
    print(a+b+c)
    
