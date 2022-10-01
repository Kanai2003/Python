def pattern(n):
    for i in range(0,n):
        for j in range (0,n-i-1):
            print(" ",end="");
        for j in range(0,i):
            ch = chr(65+j)
            print(ch,end="")
        for j in range (i+1,0,-1):
            ch = chr(64+j)
            print(ch , end="")
        print()
    for i in range(n-2,-1,-1):
        for j in range (0,n-i-1):
            print(" ",end="");
        for j in range(0,i):
            ch = chr(65+j)
            print(ch,end="")
        for j in range (i+1,0,-1):
            ch = chr(64+j)
            print(ch , end="")
        print()

pattern(5)