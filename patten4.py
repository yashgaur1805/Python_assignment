r = int(input("\nEnter number of rows : "))
for i in range(r) :
    for space in range(r-(i+1))  :
        print(" ",end = ' ')
    for j in range(i+1) :
        print("*",end = ' ')
    print("\n")
