with open("python/FilePractice.txt","a") as f:
    p = 'y'
    while(p == "y"):
        f.write(input("Enter Question \n"))
        f.write("\n")
        p = input("Type 'y' to continue :")