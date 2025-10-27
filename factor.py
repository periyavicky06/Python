
x=int(input("Give the x value :"))
y=int(input("Give the y value :"))
a= min(x,y)
factors=[]
for i in range(1,a+1):
    if (x%i==0) and (y%i==0):
        factors.append(i)

print("common factors:"," ".join(map(str,factor)))

        
