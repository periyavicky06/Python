x=int(input("Give the number of the books :"))
y=int(input("Give the price  of the books :"))
total=x*y   
if(x>=2 and x<=4):
    res=total*10//100
    print(total-res)
elif(x==5):
    res=total*20//100
    print(total-res)
elif(x>5):
    res=total*50//100
    print(total-res)
else:
    print(total)