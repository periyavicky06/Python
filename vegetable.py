a=int(input("Give the number of 1 rupee coin :"))
b=int(input("Give the number of 2 rupee coin :"))
c=int(input("Give the number of 5rupee coin :"))
d=int(input("Give the number of 10 rupee coin :"))
x=int(input("Give the number of bill rupee coin :"))
a=a*1
b=b*2
c=c*5
d=d*10
pocket=a+b+c+d
if(x==pocket):
    print("paid")
elif(x<pocket):
    res=pocket-x
    print("paid ",res)
else:
    res=pocket<x
    print("Not paid ",pocket)