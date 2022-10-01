greeting = "Good Morning"
name = "Kanai"

#concatinating two strings
c = greeting + " " + name
print(c)

print(name[3])      #print a character of a strings at the index
print(name[0:4])    #String slicing or print a sub-String  of any strings 
print(name[0:])     #is same as name[1:5]
print(name[:3])     #is same as name[0:3]

#negetive index of string means that index number from back to front 
print(name[-2])     #is same as name[3]
print(name[-4:-1])  #is same as name[1:4]

print(name[0:5:2])  #it will print by skipping 2 characters , check it positively
# here first element is starting index, second element is ending Index and last index is index is skipping number


story = "I am Kanai & I want to see my parent's happyness"  #we can use \n for new line \t for tab etc.

#functions for String
print(len(story))    #print length of story
print(story.endswith("ness"))     #it will check if String is ending with "ness"
print(story.count("a"))     #it will count number of any characters or word etc.
print(story.capitalize())   #it will print capitalized string 
print(story.find("my"))     #it will check and print index of any characters or word etc.
print(story.replace("Kanai", "Ritam"))    #it will replace Kanai with Rit


