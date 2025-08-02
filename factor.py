x=int(input("Give the x value :"))
y=int(input("Give the y value :"))
a=min(x,y)
factor=[]
for i in range(1,a+1):
    if (x%i==0) and (y%i==0):
        factor.append(i)

print(" ".join(map(str,factor)))
        