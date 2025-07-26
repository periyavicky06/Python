bowl=[10,10,10,10,10,10,10,10,9]
b1=bowl[0:3]
b2=bowl[3:6]
b3=bowl[6:9]

w1=sum(b1)
w2=sum(b2)
if(9 in bowl):
    if(w1==w2):
        if(b3[0]==b3[1]):
            print("Position is :9")
        elif(b3[0]<b3[1]):
            print("position is :7")
        else:
            print("Position is :8")
    elif(w1<w2):
        if(b1[0]==b1[1]):
            print("Position is :3")
        elif(b1[0]<b1[1]):
            print("position is: 1")
        else:
            print("position is :2")
    else:
        if(b2[0]==b2[1]):
            print("Position is :6")
        elif(b2[0]<b2[1]):
            print("position is: 4")
        else:
            print("position is :5")
else:
    print("Not 9gram ball in the bowl")
        