x=int(input("Give the x value :"))
y=int(input("Give the y value :"))
z=int(input("Give the z value :"))
if(y==z):
    dis1=y*10/100
    dis2=z*10/100
    res=dis1+dis2
    print("{:.2f}".format(x+y+z-res))
elif(x==y):
    dis1=x*10/100
    dis2=y*10/100
    res=dis1+dis2
    print("{:.2f}".format(x+y+z-res))
elif(x==z):
    dis1=x*10/100
    dis2=z*10/100
    res=dis1+dis2
    print("{:.2f}".format(x+y+z-res))
else:
    print("{:.2f}".format(x+y+z))

