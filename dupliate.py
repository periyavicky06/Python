list1=[1,2,3,4,5,6,6,6,6]
# list2=set()
# for i in list1:
#     for j in range(i+1,len(list1)):
#         if(list1[i]==list1[j]):
#             list2.add(list1[i])
#             break
# list3=list(list2)
# if(len(list3) ==0):
#     print("No duplicate ")
# else:
#     for i in range (len(list3)):
#         print(list3[i],end=" ")
        
  
for b in list1:
    if list1.count(b) >1:
        print(b)
        
        
        
