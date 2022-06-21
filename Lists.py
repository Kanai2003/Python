#creat a list using []
a = [1,2,3,4,5,]
print(a)
print(sum(a))   # sum(a) is a finction to calculate the sum of the elements

#access using index
print(a[0])

#change value using index
a[0] = 10
a[1] = 100

print(a)

#we can creat a list with items of different types 
b = ["Kanai" , 39 , 12 , 'A' , "Gr B "]
print(b)


#list slicing
friends = ["Sourav" , "Sudip" , "Ritam" , "Adrija" , "Ritwika"]
print(friends[0:2])              # we can do all the things which we can do in String 
print(friends[2:5])


#Method/function  in list 
l1 = [1, 3, 15, 9, 5]
print(l1)

l1.sort()       #sort the list
print(l1)

l1.reverse()    #reverse the lists
print(l1)   

l1.append(45)    #add a new item to the list
print(l1)

l1.insert(0,130)    #insert a  new item at any index in the list 
print(l1)

l1.pop()        #remove the item from the lists using index number
print(l1)

l1.remove()     #remove the item from the list using value
print(l1)







