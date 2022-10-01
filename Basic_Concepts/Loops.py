# in python we have two types of loop : 1. for  &  2. while

#while loop ---------------
i = 0
while i < 10:
    print(i)
    i += 1


#for loop ---------------
fruits = ["Banana", "Watermelon", "orange", "Mango"]

for items in fruits:
    print(items)

for i in range(10):      #here i will go upto range(10) means upto 9
    print(i)    

for i in range(10,20):    #we can also write range like this 
    print(i)

for i in range (20,50,2):    #we can also write range like this range(start , end , step_size)
    print(i)


#else with for loop
for i in range(50,60):
    print(i)
    if i == 55:      #if "break" condition is true then "else" will not work , and same for oposite condition
        break       #actually we use else condition when we have to check if break is working or not      
else:               #this else is optional & we can use it in also while loop
    print("For loop successfully done")



for i in range(60,70):
    if i == 65:
        break       #break use for break or exit from the loop
    print(i)



for i in range(70,80):
    if i == 75:
        continue       #continue use for go to the first part of loop without executing lower part of continue statement of the loop
    print(i)



for i in range(80,90):
    if i == 85:
        pass       # pass is besically a null statement which means to do nothing
    print(i)
