n = int(input("Give the n value :"))
if n % 2 == 0:
    print("valid")
else:
   
    if n <= 1:
        print("invalid")
    else:
        p = True
        for i in range(2, n):
            if n % i == 0:
                p = False
                break
        if p:
            print("valid")
        else:
            print("invalid")
