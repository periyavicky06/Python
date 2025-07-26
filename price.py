price=int(input("Give the price of the item :")) 
if (price<=1000):
    res=((price*10)/100)
    print("{:.2f}".format(res))
else:
    subraction=price-1000
    res1=1000*10/100
    res2=subraction*5/100
    res3=res1+res2 
    print("{:.2f}".format(res3))
