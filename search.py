a=[10,10,9,10,10,10,10,10,10]
print(a.index(9))
search=9
for i in range(len(a)):
    if(a[i]==search):
        print("Item is found:",a[i])
        break
for i in range(len(a)):
    if(a[i]%2==1):
        print("Item is found:",a[i])
