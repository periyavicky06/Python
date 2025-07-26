s=input("Give the string:")
a,e,o,u,i=0,0,0,0,0
for i in s:
    if(i=='a'):
        a=1
    elif(i=='e'):
          e=1
    elif(i=='i'):
        ie=1
    elif(i=='o'):
        o=1
    elif(i=='u'):
        u=1
    
if(a==1 and e==1 and ie==1 and o==1 and u==1):
    print("yes")
else:
    print("No")
    