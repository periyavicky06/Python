n=int(input("Give the n value :"))
list1=[]
list2=[]
for i in range(1,n+1,1):
    list1.append(i)
for j in range(1,n,2):
    list1[j]=-(1+j)
for k in range(n):
    list2.append(list1[k])
print(sum(list2))
