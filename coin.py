n=int(input("Give the amount :"))
five=n//5 #3
five1=five*5 #15
bal1=n-five1 #3
two=bal1//2 #
two1=two*2 #2
bal2=bal1-two1 #1
one=bal2//1
if(n%5 ==0):
    print("count of Rs 5:",five)
elif(n%5==2 and n%2==0):
    print("count of Rs 5:",five)
    print("Count of Rs 2:",two)
else:
    print("count of Rs 5:",five)
    print("Count of Rs 2:",two)
    print("Count of Rs 1:",one)
