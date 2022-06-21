#making own Dictionary
myDict = {
    "name" : "Kanai",
    "age" : 18,
    "Marks" : [86 , 90.4 , 9.86],
    "anotherDict" : {"name" : "Kanai"}  #a new nested dictionary
}


#printing dictionary values by using dictionary keys 
print(myDict['name'])
print(myDict['age']) 
print(myDict['Marks'])
myDict['Marks'] = [9.86 , 90.4 , 86]    #we can change/update the value of the dictionary 
print(myDict['Marks'])
print(myDict['anotherDict']['name'])
print(type(myDict['Marks']))



#methods for Dictionary
print(myDict.keys())        #print the keys of the dictionary 
print(type(myDict.keys()))

print(myDict.values())      #print the values of the dictionary 
print(type(myDict.values()))

print(myDict.items())       #print the (keys , values) pairs of all contents in the dictionary 
print(type(myDict.items()))


#creating a new dictionary
update_dict = {
    "Ritam" : "Friend",
    "Shubham" : "Friend",
    "Adrija" : "Friend",
    "Ritwika" : "Friend"
}

myDict.update(update_dict)      #updating/marging  myDict dictionary  with the new dictionary named as update_dict 
print(myDict)



print(myDict.get("Ritam"))      #to get valus of the dictionary

# V V I : difference between this two functions
#print(myDict["Ritam2"])           #line will return error because of unavailability of "Ritam2"
print(myDict.get("Ritam2"))        #But this line will return None because  of unavailability of "Ritam2"



