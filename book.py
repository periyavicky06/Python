book=int(input("Give the number of the books:"))
y=int(input("Give the price of the book :"))
y=book*y
if(book>=2 and book<=4):
    res=(y*10)//100
    print(y-res)
elif(book==5):
    res=(y*20)//100
    print(y-res)
elif(book>5):
    res=(y*50)/100
    print(y-res)
else:
    print("No discount is applied")
