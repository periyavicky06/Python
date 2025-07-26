n=int(input("Give amount :")) 
coin5=n//5  
n=n%5 

coin2=n//2 
n=n%2 
coin1=n 
if(coin5>0):
    print("Count of Rs 5:",coin5)
if(coin2>0):
    print("Count of Rs 2:",coin2)
if(coin1>0):
    print("Count of Rs 1:",coin1)



