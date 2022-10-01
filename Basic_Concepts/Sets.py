a = {1,3,5,7,1}     #set is a collection of non-repetative elements 
print(type(a))
print(a)

# An empty set can be created usingthe below :
b = set()       #IF we inialize like " b = {} " that will be Dictionary not a set 
print(type(b))


#Methods in set
b.add(1)    #add a new element to the set
b.add(5)    
b.add((3,7,9))  #we can add a tuple in the set but we can't add list or Dictionary(because dictionary and list can be change)

print(b)

print(len(b))   #print the length of the set

b.remove(5)    #remove a new element from the set
print(b)    

print(b.pop())    #remove the element from the Set and print/return the removed value
print(b)

b.union({3,5})      #union the elements  in the Set

b.intersection({3,5}) #intersect the elements in the set

b.clear()    #clear the Set 
print(b)

