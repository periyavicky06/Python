str1=input("Give the first string :")
s1=[]
str2=input("Give the second string :")
s2=[]
for i in range(len(str1)):
    if(str1[i]=='a'or str1[i]=='e'or str1[i]=='i'or str1[i]=='o'or str1[i]=='u'):
        s1.append(str1[i])
for i in range(len(str2)):
    if(str2[i]=='a'or str2[i]=='e'or str2[i]=='i'or str2[i]=='o'or str2[i]=='u'):
        s2.append(str2[i])
        
if(len(str1)-len(s1)<=len(str2)-len(s2)):
    print(str2)
else:
    print(str1)
        