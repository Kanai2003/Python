# write a file------------------------
f = open("File.txt", 'w')
f.write("Please write this to the file.\nThank You")
f.close()



#appending a new line to the end of the file-------------------
f = open("File.txt", 'a')
f.write(" I am appending a new line")
f.close()



#reading a file-------------------------------
# f = open("File.txt",'r')  #we can define like this way 'r' is for read mode 
f = open('File.txt')       #By default mode is 'r'/read

# data = f.read()     #.read() function to read the contents of the file
# print(data)
# print(f.read(5))    #we can also define like this to read 5 characters

print(f.readline())   # .readline() function is use  to read a line of the file
print(f.readline())   #we can also define like this to read next line of the file

f.close()       #close the file 



#using "with" statement -------------------------------
#Best way to open and close the file is by using "with" statement like this because we don't need to close 

with open('File.txt', 'r') as f:    
    print(f.read().lower())   # ".lower()" function is used to read the file's all contents in lower case


# os.remove('File.txt')     # os.remove(file_name) function is use to remove/delete a file
                            # to use os.remove(file_name) function we need to import "os"

